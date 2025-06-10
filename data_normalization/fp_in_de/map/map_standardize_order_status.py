# type: ignore
"""
Order Status Standardization
Standardize order status codes to uppercase:
"""

order_statuses = ["pending", "SHIPPED", "delivered", "Cancelled", "processing"]

order_statuses_standardized = map(lambda x:x.upper(), order_statuses)

print(list(order_statuses_standardized))