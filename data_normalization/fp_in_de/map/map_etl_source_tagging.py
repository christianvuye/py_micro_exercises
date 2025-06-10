# type: ignore
"""
ETL Source System Tagging
Add source system identifier to each record for data lineage tracking:
"""

customer_records = [
    {"id": 1001, "name": "John Smith"},
    {"id": 1002, "name": "Jane Doe"},
    {"id": 1003, "name": "Bob Wilson"}
]
source_system = "CRM_PROD"

# Expected output: [
#   {"id": 1001, "name": "John Smith", "source_system": "CRM_PROD"},
#   {"id": 1002, "name": "Jane Doe", "source_system": "CRM_PROD"},
#   {"id": 1003, "name": "Bob Wilson", "source_system": "CRM_PROD"}
# ]

customer_records_source_system = map(lambda x:dict(x, source_system=source_system), customer_records)
print(list(customer_records_source_system))

customer_records_source_system = map(lambda x:{**x,'source_system': source_system}, customer_records)
print(list(customer_records_source_system))