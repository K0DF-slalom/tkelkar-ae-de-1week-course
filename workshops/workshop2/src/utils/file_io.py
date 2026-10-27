import csv
import os
from typing import Iterable, Sequence


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def read_csv_rows(path: str) -> list[dict[str, str]]:
    with open(path, "r", newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def write_csv(path: str, header: Sequence[str], rows: Iterable[Sequence[object]]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(rows)
