"""
Create a class called `Inventory` with class variable `total_items = 0`. When items are added 
or removed, update both the instance's `quantity` and the class's `total_items`.

Your task: Define Inventory class that tracks individual and total quantities
Test it with:
inv1 = Inventory("Apples", 50)
inv2 = Inventory("Bananas", 30)
print(Inventory.total_items)  # Should print 80
inv1.add_items(20)
print(Inventory.total_items)  # Should print 100
"""

class Inventory:
    total_items = 0

    def __init__(self, fruit, quantity):
        self.fruit = fruit
        self.quantity = quantity
        Inventory.total_items += quantity
    
    def add_items(self, quantity_to_add):
        self.quantity += quantity_to_add
        Inventory.total_items += quantity_to_add
    
inv1 = Inventory("Apples", 50)
inv2 = Inventory("Bananas", 30)
print(Inventory.total_items)  # Should print 80
inv1.add_items(20)
print(Inventory.total_items)  # Should print 100