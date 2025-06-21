"""
Valid Product Record Filtering
Filter out product records with missing or invalid data before loading into the data warehouse:
"""

product_catalog = [
    {"sku": "PROD001", "name": "Laptop Pro", "price": 1299.99, "category": "Electronics"},
    {"sku": "PROD002", "name": "", "price": 45.99, "category": "Books"},
    {"sku": "PROD003", "name": "Wireless Mouse", "price": 0, "category": "Electronics"},
    {"sku": "", "name": "Coffee Mug", "price": 12.99, "category": "Kitchen"},
    {"sku": "PROD005", "name": "Programming Book", "price": 59.99, "category": ""},
    {"sku": "PROD006", "name": "USB Cable", "price": 15.99, "category": "Electronics"},
    {"sku": "PROD007", "name": "Notebook", "price": 8.99, "category": "Office"},
    {"sku": "PROD008", "name": "Headphones", "price": None, "category": "Electronics"},
    {"sku": "PROD009", "name": "Water Bottle", "price": 25.99, "category": "Sports"}
]

# Expected output: Products that have:
# - Non-empty SKU
# - Non-empty name  
# - Price > 0 and not None
# - Non-empty category
# Should return: PROD001, PROD006, PROD007, PROD009

def not_missing_data(product: dict) -> bool:
    for product_detail in product.values():
        if not product_detail:
            return False
        else:
            continue
    return True

valid_records = filter(not_missing_data, product_catalog)
print(*(valid_record["sku"] for valid_record in valid_records), sep=", ")