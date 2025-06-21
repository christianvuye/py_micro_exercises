"""
High-Value Transaction Filtering
Filter transactions above a certain threshold for fraud monitoring and VIP customer analysis:
"""

transactions = [
    {"transaction_id": "T001", "amount": 2500.00, "customer_id": "C123"},
    {"transaction_id": "T002", "amount": 45.99, "customer_id": "C456"},
    {"transaction_id": "T003", "amount": 15000.00, "customer_id": "C789"},
    {"transaction_id": "T004", "amount": 250.50, "customer_id": "C321"},
    {"transaction_id": "T005", "amount": 5000.00, "customer_id": "C654"},
    {"transaction_id": "T006", "amount": 75.25, "customer_id": "C987"},
    {"transaction_id": "T007", "amount": 12500.00, "customer_id": "C111"},
    {"transaction_id": "T008", "amount": 99.99, "customer_id": "C222"}
]

# Expected output: All transactions with amount >= $1000
# Should return: T001 ($2500), T003 ($15000), T005 ($5000), T007 ($12500)

def over_thousand(transaction: dict) -> bool:
    return True if transaction["amount"] >= 1000 else False

high_value_transactions = filter(over_thousand, transactions)
print(*(
    high_value_transaction["transaction_id"] + " ($" + 
    str(int(high_value_transaction["amount"])) + ")" 
    for high_value_transaction in list(high_value_transactions)
), sep=',')