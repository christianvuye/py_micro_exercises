# type: ignore
"""
Multi-Source Data Integration
Transform and merge data from multiple systems with different schemas into a unified format:
1. Create two different functions to transform each data source into the unified format
2. Use map() to transform both datasets
3. Combine the results into a single list
"""

# Data from CRM system
crm_data = [
    {"client_id": "CRM001", "company_name": "TechCorp", "revenue": 50000, "industry": "Technology"},
    {"client_id": "CRM002", "company_name": "RetailCo", "revenue": 75000, "industry": "Retail"},
    {"client_id": "CRM003", "company_name": "FinanceInc", "revenue": 120000, "industry": "Finance"}
]

# Data from Sales system (different field names, different format)
sales_data = [
    {"customer_ref": "SAL_001", "org_name": "TechCorp Inc.", "total_sales": "50,000", "sector": "Tech"},
    {"customer_ref": "SAL_002", "org_name": "RetailCo LLC", "total_sales": "75,000", "sector": "Retail"}, 
    {"customer_ref": "SAL_003", "org_name": "FinanceInc Corp", "total_sales": "120,000", "sector": "Financial"}
]

# Expected unified output:
# [
#   {"id": "CRM001", "name": "TechCorp", "revenue": 50000, "category": "Technology", "source": "CRM"},
#   {"id": "CRM002", "name": "RetailCo", "revenue": 75000, "category": "Retail", "source": "CRM"},
#   {"id": "CRM003", "name": "FinanceInc", "revenue": 120000, "category": "Finance", "source": "CRM"},
#   {"id": "SAL_001", "name": "TechCorp Inc.", "revenue": 50000, "category": "Tech", "source": "Sales"},
#   {"id": "SAL_002", "name": "RetailCo LLC", "revenue": 75000, "category": "Retail", "source": "Sales"},
#   {"id": "SAL_003", "name": "FinanceInc Corp", "revenue": 120000, "category": "Financial", "source": "Sales"}
# ]

#you would be better off using type hints here to specify that this parameter expects a dict, instead of naming the variable that way, but for now OK

"""
type hints:

from typing import Dict, Any

# Using type hints for clarity
def transform_crm_data(crm_record: Dict[str, Any]) -> Dict[str, Any]:
    # ... function body ...
"""


def transform_crm_data(crm_data_dict): 
    transformed_data = {}
    transformed_data["id"] = crm_data_dict["client_id"]
    transformed_data["name"] = crm_data_dict["company_name"]
    transformed_data["revenue"] = crm_data_dict["revenue"]
    transformed_data["category"] = crm_data_dict["industry"]
    transformed_data["source"] = "CRM"
    return transformed_data

def transform_sales_data(sales_data_dict):
    transformed_data = {}
    transformed_data["id"] = sales_data_dict["customer_ref"]
    transformed_data["name"] = sales_data_dict["org_name"]
    transformed_data["revenue"] = int(sales_data_dict["total_sales"].replace(",",""))
    transformed_data["category"] = sales_data_dict["sector"]
    transformed_data["source"] = "Sales"
    return transformed_data


transformed_crm_data = map(transform_crm_data, crm_data)
transformed_sales_data = map(transform_sales_data, sales_data)

final_list = list(transformed_crm_data) + list(transformed_sales_data)
print([data for data in final_list])


# More concise version of CRM function
"""
def transform_crm_data_pythonic(record: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": record["client_id"],
        "name": record["company_name"],
        "revenue": record["revenue"],
        "category": record["industry"],
        "source": "CRM"
    }

# More concise version of Sales function
def transform_sales_data_pythonic(record: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": record["customer_ref"],
        "name": record["org_name"],
        "revenue": int(record["total_sales"].replace(",", "")),
        "category": record["sector"],
        "source": "Sales"
    }
"""