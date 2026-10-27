import os

from src.models.customer import Customer
from src.utils.file_io import read_csv_rows


class CustomerRepository:
    def __init__(self, input_dir: str) -> None:
        self._customers_path = os.path.join(input_dir, "customer.csv")

    def list_customers(self) -> list[Customer]:
        customers: list[Customer] = []
        for row in read_csv_rows(self._customers_path):
            customers.append(Customer(id=row["id"], age=int(row["age"])))
        return customers
