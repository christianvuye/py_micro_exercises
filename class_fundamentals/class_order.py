"""
You're building a customer order system. Create an Order class that calculates totals, 
applies discounts, and tracks order status through different stages.

Your task: Create an Order class for e-commerce
Test with:
order = Order("ORD001", [{"item": "Laptop", "price": 1000, "qty": 1}])
print(order.calculate_total())  # Should print 1000
order.apply_discount(0.1)  # 10% discount
print(order.calculate_total())  # Should print 900.0
"""

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
    
    def calculate_total(self):
        running_total = 0
        for item_detail in self.items:
            running_total += item_detail["price"] * item_detail["qty"]
        return running_total
    
    def apply_discount(self, amount):
        for item_detail in self.items:
            item_detail["price"] *= (1-amount)

order = Order("ORD001", [{"item": "Laptop", "price": 1000, "qty": 1}])
print(order.calculate_total())  # Should print 1000
order.apply_discount(0.1)  # 10% discount
print(order.calculate_total())  # Should print 900.0