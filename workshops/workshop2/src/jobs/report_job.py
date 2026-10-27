import os

from src.data_access.customer_repository import CustomerRepository
from src.data_access.sales_repository import SalesRepository
from src.services.reporting_service import ReportingService
from src.utils.file_io import ensure_dir, write_csv


def run_reports() -> None:
    input_dir = os.path.join("test_data", "source")
    output_dir = os.path.join("test_data", "output")
    ensure_dir(output_dir)

    sales_repository = SalesRepository(input_dir=input_dir)
    customer_repository = CustomerRepository(input_dir=input_dir)
    reporting_service = ReportingService()

    sales = sales_repository.list_sales()

    write_csv(
        path=os.path.join(output_dir, "report1.csv"),
        header=["product_id", "total_quantity"],
        rows=reporting_service.report1_rows(sales),
    )
    print("Report 1 generated")

    customers = customer_repository.list_customers()
    write_csv(
        path=os.path.join(output_dir, "report2.csv"),
        header=["age_band", "total_revenue"],
        rows=reporting_service.report2_rows(sales=sales, customers=customers),
    )
    print("Report 2 generated")

    write_csv(
        path=os.path.join(output_dir, "report3.csv"),
        header=["product_id_1", "product_id_2", "order_count"],
        rows=reporting_service.report3_rows(sales),
    )
    print("Report 3 generated")


if __name__ == "__main__":
    run_reports()
