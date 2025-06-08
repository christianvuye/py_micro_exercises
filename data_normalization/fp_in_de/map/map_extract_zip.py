# type: ignore
"""
Customer Address Standardization: Extract ZIP codes from full addresses
"""

customer_addresses = [
    "123 Main St, New York, NY 10001",
    "456 Oak Ave, Los Angeles, CA 90210", 
    "789 Pine Rd, Chicago, IL 60601",
    "321 Elm St, Houston, TX 77001"
]

zip_codes = map(lambda x:x[-5:], customer_addresses)

print(list(zip_codes))