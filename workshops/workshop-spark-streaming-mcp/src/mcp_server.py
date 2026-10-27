"""MCP server for Postgres-backed stock insights."""

import os
from typing import Any, Dict, List, Optional

import psycopg2
from psycopg2.extras import RealDictCursor
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount
import uvicorn


MAX_LIMIT = 500


def _get_env(name: str, default: str) -> str:
    return os.getenv(name, default)


def _db_config() -> Dict[str, Any]:
    return {
        "host": _get_env("POSTGRES_HOST", "postgres"),
        "port": int(_get_env("POSTGRES_PORT", "5432")),
        "dbname": _get_env("POSTGRES_DB", "sparkdb"),
        "user": _get_env("POSTGRES_USER", "sparkuser"),
        "password": _get_env("POSTGRES_PASSWORD", "sparkpass"),
    }


def _normalize_limit(limit: int) -> int:
    try:
        limit_value = int(limit)
    except (TypeError, ValueError):
        limit_value = 10

    if limit_value < 1:
        return 1

    return min(limit_value, MAX_LIMIT)


def _run_query(sql: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
    with psycopg2.connect(**_db_config()) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params or ())
            rows = cur.fetchall()
            return [dict(row) for row in rows]


mcp = FastMCP("Stock Insights", json_response=True)


@mcp.tool()
def latest_prices(limit: int = 10) -> List[Dict[str, Any]]:
    """Return the latest price per symbol."""
    limit_value = _normalize_limit(limit)
    sql = """
        SELECT symbol, latest_price, last_trade_time, trade_type
        FROM latest_prices
        ORDER BY last_trade_time DESC
        LIMIT %s
    """
    return _run_query(sql, (limit_value,))


@mcp.tool()
def recent_trades(limit: int = 20, symbol: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return recent trades, optionally filtered by symbol."""
    limit_value = _normalize_limit(limit)
    if symbol:
        sql = """
            SELECT trade_id, symbol, price, quantity, trade_value, trade_type, timestamp
            FROM stock_trades
            WHERE symbol = %s
            ORDER BY timestamp DESC
            LIMIT %s
        """
        params = (symbol, limit_value)
    else:
        sql = """
            SELECT trade_id, symbol, price, quantity, trade_value, trade_type, timestamp
            FROM stock_trades
            ORDER BY timestamp DESC
            LIMIT %s
        """
        params = (limit_value,)
    return _run_query(sql, params)


@mcp.tool()
def window_aggregates(
    limit: int = 20, symbol: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Return windowed aggregates, optionally filtered by symbol."""
    limit_value = _normalize_limit(limit)
    if symbol:
        sql = """
            SELECT symbol, window_start, window_end, avg_price, min_price, max_price,
                total_volume, trade_count, total_value
            FROM stock_aggregates
            WHERE symbol = %s
            ORDER BY window_start DESC
            LIMIT %s
        """
        params = (symbol, limit_value)
    else:
        sql = """
            SELECT symbol, window_start, window_end, avg_price, min_price, max_price,
                total_volume, trade_count, total_value
            FROM stock_aggregates
            ORDER BY window_start DESC
            LIMIT %s
        """
        params = (limit_value,)
    return _run_query(sql, params)


@mcp.tool()
def symbol_summary(days: int = 1) -> List[Dict[str, Any]]:
    """Return per-symbol daily summaries for the last N days."""
    try:
        days_value = int(days)
    except (TypeError, ValueError):
        days_value = 1

    if days_value < 1:
        days_value = 1

    sql = """
        SELECT symbol, trade_date, trade_count, total_volume, total_value,
            avg_price, min_price, max_price
        FROM daily_summary
        WHERE trade_date >= CURRENT_DATE - %s
        ORDER BY trade_date DESC, symbol ASC
    """
    return _run_query(sql, (days_value,))


def build_app() -> Starlette:
    return Starlette(routes=[Mount("/", app=mcp.sse_app("/"))])


if __name__ == "__main__":
    host = _get_env("MCP_HOST", "0.0.0.0")
    port = int(_get_env("MCP_PORT", "3333"))
    uvicorn.run(build_app(), host=host, port=port)
