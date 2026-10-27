# Schema

## Input data

`test_data/source/product.csv`  
Catalog of products sold by the shop.

| Column | Description |
| --- | --- |
| `id` | Product identifier. |
| `product_name` | Product name. |
| `createdOn` | Product creation timestamp. |

`test_data/source/customer.csv`  
Customer master data.

| Column | Description |
| --- | --- |
| `id` | Customer identifier. |
| `first_name` | Customer first name. |
| `last_name` | Customer last name. |
| `age` | Customer age in years. |

`test_data/source/sales.csv`  
Line items for customer purchases.

| Column | Description |
| --- | --- |
| `id` | Sales line identifier. |
| `order_id` | Order identifier (same value groups items bought together). |
| `product_id` | Product identifier from `product.csv`. |
| `customer_id` | Customer identifier from `customer.csv`. |
| `quantity` | Quantity purchased for the line item. |
| `unit_price` | Unit price at time of purchase. |
| `purchase_time` | Purchase timestamp for the order. |

## Report outputs

`test_data/output/report1.csv`  
Product popularity totals by product across all orders.

| Column | Description |
| --- | --- |
| `product_id` | Product identifier from `product.csv`. |
| `total_quantity` | Total quantity sold for the product across all orders. |

`test_data/output/report2.csv`  
Revenue totals by customer age band.

| Column | Description |
| --- | --- |
| `age_band` | Age bucket: `20-29`, `30-39`, or `40-50`. |
| `total_revenue` | Sum of `quantity * unit_price` for customers in the age band. |

`test_data/output/report3.csv`  
Product affinity counts based on co-purchases in the same order.

| Column | Description |
| --- | --- |
| `product_id_1` | First product in the pair (smaller id). |
| `product_id_2` | Second product in the pair (larger id). |
| `order_count` | Number of distinct orders where the pair appears together. |
