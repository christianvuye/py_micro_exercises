# type: ignore
"""
Convert USD prices to EUR (exchange rate: 1 USD = 0.85 EUR)
"""
usd_prices = [100.00, 250.50, 75.25, 500.00, 150.75]

usd_to_eur = map(lambda x:round(0.85*x,2), usd_prices)

print(list(usd_to_eur))
