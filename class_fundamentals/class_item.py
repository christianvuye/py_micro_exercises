"""
You're building an inventory management system for a warehouse. Create an Item class 
that tracks product details and stock levels with automatic reorder alerts.

Your task: Create an Item class for inventory management
Test with:
item = Item("Widget", "W001", 5, 10)  # name, sku, current_stock, reorder_level
print(item.needs_reorder())  # Should print True (5 <= 10)
item.add_stock(20)
print(item.needs_reorder())  # Should print False (25 > 10)
"""

class Item:
    def __init__(self, name, sku, current_stock, reorder_level):
        self.name = name
        self.sku = sku
        self.current_stock = current_stock
        self.reorder_level = reorder_level
    
    def needs_reorder(self):
        return self.current_stock <= self.reorder_level
    
    def add_stock(self, quantity):
        self.current_stock += quantity

item = Item("Widget", "W001", 5, 10)  # name, sku, current_stock, reorder_level
print(item.needs_reorder())  # Should print True (5 <= 10)
item.add_stock(20)
print(item.needs_reorder())  # Should print False (25 > 10)