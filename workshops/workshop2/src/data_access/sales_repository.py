import os

from src.models.sales import Sale
from src.utils.file_io import read_csv_rows


class SalesRepository:
    def __init__(self, input_dir: str) -> None:
        self._sales_path = os.path.join(input_dir, "sales.csv")

    def list_sales(self) -> list[Sale]:
        sales: list[Sale] = []
        for row in read_csv_rows(self._sales_path):
            sales.append(
                Sale(
                    order_id=row["order_id"],
                    customer_id=row["customer_id"],
                    product_id=row["product_id"],
                    quantity=int(row["quantity"]),
                    unit_price=float(row["unit_price"]),
                )
            )
        return sales
