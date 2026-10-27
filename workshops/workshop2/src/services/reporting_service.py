from collections import defaultdict

from src.models.customer import Customer
from src.models.sales import Sale


class ReportingService:
    def report1_rows(self, sales: list[Sale]) -> list[list[object]]:
        totals_by_product: dict[str, int] = defaultdict(int)
        for sale in sales:
            totals_by_product[sale.product_id] += sale.quantity

        return [
            [product_id, totals_by_product[product_id]]
            for product_id in sorted(totals_by_product.keys(), key=int)
        ]

    def report2_rows(self, sales: list[Sale], customers: list[Customer]) -> list[list[object]]:
        age_by_customer = {customer.id: customer.age for customer in customers}
        revenue_by_band: dict[str, float] = defaultdict(float)

        for sale in sales:
            age = age_by_customer[sale.customer_id]
            revenue = sale.quantity * sale.unit_price

            if 20 <= age <= 29:
                band = "20-29"
            elif 30 <= age <= 39:
                band = "30-39"
            else:
                band = "40-50"

            revenue_by_band[band] += revenue

        return [[band, f"{revenue_by_band[band]:.2f}"] for band in ["20-29", "30-39", "40-50"]]

    def report3_rows(self, sales: list[Sale]) -> list[list[object]]:
        products_by_order: dict[str, list[str]] = defaultdict(list)
        for sale in sales:
            products_by_order[sale.order_id].append(sale.product_id)

        pair_counts: dict[tuple[str, str], int] = defaultdict(int)
        for products in products_by_order.values():
            unique_products = sorted(set(products), key=int)
            for i in range(len(unique_products)):
                for j in range(i + 1, len(unique_products)):
                    pair = (unique_products[i], unique_products[j])
                    pair_counts[pair] += 1

        return [
            [product_id_1, product_id_2, pair_counts[(product_id_1, product_id_2)]]
            for product_id_1, product_id_2 in sorted(pair_counts.keys(), key=lambda p: (int(p[0]), int(p[1])))
        ]
