"""
Create a class called `ShoppingCart` with instance variable `items` (empty list). 
Add methods `add_item`, `remove_item`, and `get_total` that calculates total price.

Your task: Define ShoppingCart class with item management
Test it with:
cart = ShoppingCart()
cart.add_item({"name": "Apple", "price": 1.50})
cart.add_item({"name": "Bread", "price": 2.00})
print(cart.get_total())  # Should print 3.5
cart.remove_item("Apple")
print(cart.get_total())  # Should print 2.0
"""

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        for item_dict in self.items:
            if item_dict["name"] == item:
                self.items.remove(item_dict)
    
    def get_total(self):
        running_total = 0
        for item in self.items:
            running_total += item["price"]
        return running_total

cart = ShoppingCart()
cart.add_item({"name": "Apple", "price": 1.50})
cart.add_item({"name": "Bread", "price": 2.00})
print(cart.items)
print(cart.get_total())  # Should print 3.5
cart.remove_item("Apple")
print(cart.items)
print(cart.get_total())  # Should print 2.0