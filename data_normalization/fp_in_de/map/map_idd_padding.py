# type: ignore
"""
Database ID Padding
Pad customer IDs with leading zeros to make them 8 digits (common for legacy system integration)
"""

customer_ids = [123, 4567, 89, 12345, 678]

# first approach, without knowing about zfill str method
customer_ids_padded = map(lambda x: "0" * (8 - len(str(x))) + str(x), customer_ids)
print(list(customer_ids_padded))

# with zfill method
customer_ids_padded = map(lambda x:str(x).zfill(8), customer_ids)
print(list(customer_ids_padded))