# type: ignore
"""
Data Warehouse Key Generation
Generate surrogate keys by combining business keys with prefixes:
"""

business_data = [
    {"customer_id": "CUST001", "product_id": "PROD123"},
    {"customer_id": "CUST002", "product_id": "PROD456"},
    {"customer_id": "CUST003", "product_id": "PROD789"}
]

# Expected output: ["CUST001_PROD123", "CUST002_PROD456", "CUST003_PROD789"]

composite_keys = map(lambda x:x["customer_id"]+"_"+x["product_id"], business_data)
print(list(composite_keys))