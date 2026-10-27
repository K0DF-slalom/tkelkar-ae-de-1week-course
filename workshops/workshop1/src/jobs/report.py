import csv
import os
from collections import defaultdict
from datetime import datetime


def report1() -> None:
    input_dir = os.path.join("test_data", "source")
    output_dir = os.path.join("test_data", "output")
    os.makedirs(output_dir, exist_ok=True)

    sales_path = os.path.join(input_dir, "sales.csv")
    totals_by_product = defaultdict(int)

    with open(sales_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_id = row["product_id"]
            quantity = int(row["quantity"])
            totals_by_product[product_id] += quantity

    output_path = os.path.join(output_dir, "report1.csv")
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id", "total_quantity"])
        for product_id in sorted(totals_by_product.keys(), key=int):
            writer.writerow([product_id, totals_by_product[product_id]])


def report2() -> None:
    input_dir = os.path.join("test_data", "source")
    output_dir = os.path.join("test_data", "output")
    os.makedirs(output_dir, exist_ok=True)

    customers_path = os.path.join(input_dir, "customer.csv")
    sales_path = os.path.join(input_dir, "sales.csv")

    age_by_customer = {}
    with open(customers_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            age_by_customer[row["id"]] = int(row["age"])

    revenue_by_band = defaultdict(float)
    with open(sales_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            customer_id = row["customer_id"]
            age = age_by_customer[customer_id]
            quantity = int(row["quantity"])
            unit_price = float(row["unit_price"])
            revenue = quantity * unit_price

            if 20 <= age <= 29:
                band = "20-29"
            elif 30 <= age <= 39:
                band = "30-39"
            else:
                band = "40-50"

            revenue_by_band[band] += revenue

    output_path = os.path.join(output_dir, "report2.csv")
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["age_band", "total_revenue"])
        for band in ["20-29", "30-39", "40-50"]:
            writer.writerow([band, f"{revenue_by_band[band]:.2f}"])


def report3() -> None:
    input_dir = os.path.join("test_data", "source")
    output_dir = os.path.join("test_data", "output")
    os.makedirs(output_dir, exist_ok=True)

    sales_path = os.path.join(input_dir, "sales.csv")
    products_by_order = defaultdict(list)

    with open(sales_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            order_id = row["order_id"]
            product_id = row["product_id"]
            products_by_order[order_id].append(product_id)

    pair_counts = defaultdict(int)
    for order_id, products in products_by_order.items():
        unique_products = sorted(set(products), key=int)
        for i in range(len(unique_products)):
            for j in range(i + 1, len(unique_products)):
                pair = (unique_products[i], unique_products[j])
                pair_counts[pair] += 1

    output_path = os.path.join(output_dir, "report3.csv")
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id_1", "product_id_2", "order_count"])
        for pair in sorted(pair_counts.keys(), key=lambda p: (int(p[0]), int(p[1]))):
            writer.writerow([pair[0], pair[1], pair_counts[pair]])


if __name__ == "__main__":
    report1()
    print("Report 1 generated")
    report2()
    print("Report 2 generated")
    report3()
    print("Report 3 generated")