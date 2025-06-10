# type: ignore
"""
Sales Commission Calculation
Calculate sales commission based on sale amount (5% for amounts over $1000, 3% otherwise):
"""

sales_amounts = [500, 1200, 800, 2000, 1500]
# Expected output: [15.0, 60.0, 24.0, 100.0, 75.0]

sales_amounts_commissions = map(lambda x: 0.05 * x if x > 1000 else 0.03 * x, sales_amounts)

print(list(sales_amounts_commissions))