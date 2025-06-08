# type: ignore
"""
Product SKU Normalization: Convert product SKUs to uppercase and remove spaces.
"""

product_skus = ["abc-123", "xyz 456", "def-789", "ghi 012"]

product_skus_normalized = map(lambda x:x.replace(" ", "").upper(), product_skus)

print(list(product_skus_normalized))