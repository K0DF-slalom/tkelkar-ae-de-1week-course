from dataclasses import dataclass


@dataclass(frozen=True)
class Sale:
    order_id: str
    customer_id: str
    product_id: str
    quantity: int
    unit_price: float
