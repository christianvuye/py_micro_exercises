# type: ignore
"""
Data Quality Score Assignment
Assign data quality scores based on completeness (1 point per non-empty field):
"""

customer_profiles = [
    {"name": "John", "email": "john@email.com", "phone": "", "address": "123 Main St"},
    {"name": "Jane", "email": "", "phone": "555-1234", "address": ""},
    {"name": "", "email": "bob@email.com", "phone": "555-5678", "address": "456 Oak Ave"}
]

# Expected output: [3, 2, 3] (count of non-empty fields)

def count_non_empty_fields(list_of_dicts):
    non_empty_fields_list = []
    for dictionary in list_of_dicts:
        count = len(dictionary)
        for field in dictionary.values():
            if not field:
                count -= 1
        non_empty_fields_list.append(count)
    return non_empty_fields_list

print(count_non_empty_fields(customer_profiles))

count_non_empty_fields_fp = map(count_non_empty_fields, customer_profiles)

print(list(count_non_empty_fields_fp))