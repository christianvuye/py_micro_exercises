"""
Create an inventory management system that tracks products and monitors stock levels across multiple locations.

Concepts practiced:
- Class-level tracking with dictionaries (inventory registry)
- Conditional list management (stock alerts, reorder logic)
- Status monitoring (availability, stock levels, alerts)

Business Requirements:
- Track individual products with quantities and locations
- Maintain system-wide inventory registry
- Monitor stock levels and generate alerts
- Support multiple warehouse locations
- Handle product status changes and stock movements

Your stakeholder says: "We need to track inventory across our warehouses. Each product 
should know its stock level, location, and whether we need to reorder. The system should 
keep track of all products and tell us which ones are running low."

# Test your class:
item1 = InventoryItem("Laptop", quantity=50, location="Warehouse A")
item2 = InventoryItem("Mouse", quantity=5, location="Warehouse B") 
item3 = InventoryItem("Keyboard", quantity=200, location="Warehouse A")

item1.update_quantity(-10)  # Sell 10 laptops
item2.update_quantity(-3)   # Sell 3 mice

print(item1.get_status())                    # Expected: status info
print(item2.is_low_stock())                  # Expected: True (only 2 left)
print(InventoryItem.get_low_stock_items())   # Expected: list of items needing reorder
print(InventoryItem.get_inventory_summary()) # Expected: system-wide summary
"""

from typing import List

class InventoryItem:
    """
    InventoryItem class for managing products across locations.

    Features:
    - Validates product name, quantity, and location.
    - Tracks low stock items (quantity < 5) and all inventory.
    - Allows quantity updates and status checks.
    - Provides class-level summaries for low stock and inventory.
    """

    PRODUCTS: List[str] = ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"]
    LOCATIONS: List[str] = ["Warehouse A", "Warehouse B", "Warehouse C", "Store Front"]

    total_inventory: List['InventoryItem'] = []

    def __init__(self, product_name: str, quantity: int, location: str) -> None:
        """
        Initializes an InventoryItem instance with validation.

        Args:
            product_name (str): The name of the product. Must be in InventoryItem.PRODUCTS.
            quantity (int): The quantity of the product in stock. Must be an integer.
            location (str): The location where the product is stored. Must be in InventoryItem.LOCATIONS.

        Raises:
            ValueError: If product_name is not in the list of products or location is not in the list of locations.
            TypeError: If quantity is not an integer.

        Side Effects:
            - Adds the item to the class-level total_inventory list.
            - If the item is low in stock, adds it to the class-level low_stock_items dictionary.
        """
        if product_name not in InventoryItem.PRODUCTS:
            raise ValueError(f"{product_name} is not in the list of products")
        if location not in InventoryItem.LOCATIONS:
            raise ValueError(f"{location} is not in the list of locations")
        if not isinstance(quantity, int):
            raise TypeError(f"{quantity} is not an integer!")

        self.product_name = product_name
        self.quantity = quantity
        self.location = location

        InventoryItem.total_inventory.append(self) #store the instance directly

    def update_quantity(self, amount: int) -> None:
        """
        Updates the quantity of the inventory item by a specified amount.

        Args:
            amount (int): The amount to update the quantity by. Positive values increase the quantity,
            negative values decrease it.

        Raises:
            TypeError: If the provided amount is not an integer.
            ValueError: If attempting to decrease the quantity below zero.

        Side Effects:
            - Updates the instance's quantity.
            - Updates the class-level low_stock_items dictionary if the item becomes low in stock.
            - Removes the items from the class-level low_stock_items dictionary if the item is no longer low in stock

        Returns:
            None
        """
        if not isinstance(amount, int):
            raise TypeError(f"{amount} is not an integer!")

        if amount < 0 and self.quantity < abs(amount):
            raise ValueError(f"Cannot sell {abs(amount)} items as there are only {self.quantity} in stock")

        self.quantity += amount
        
    def is_low_stock(self) -> bool:
        """
        Check if the inventory item is low in stock.

        Returns:
            bool: True if the item's quantity is less than 5, indicating low stock; False otherwise.
        """
        return self.quantity < 5

    def get_status(self) -> str:
        """
        Returns a formatted string representing the current status of the inventory item.

        The status includes the product name, quantity, location, and a stock status
        ("LOW STOCK" if the item is considered low in stock, otherwise "OK").

        Returns:
            str: A formatted string with product details and stock status.
        """
        status = "LOW STOCK" if self.is_low_stock() else "OK"
        return (
            f"Product: {self.product_name} | "
            f"Quantity: {self.quantity} | "
            f"Location: {self.location} | "
            f"Status: {status}"
        )

    @classmethod  
    def get_low_stock_items(cls):
        """
        Class method that returns a formatted string listing all items with low stock.
        If there are no low stock items, returns a message indicating so.

        Returns:
            str: A message listing low stock items and their quantities, or a message if none exist.
        """
        low_stock = [item for item in cls.total_inventory if item.is_low_stock()]
        if not low_stock:
            return "No low stock items."
        return "\n".join(f"{item.product_name}: {item.quantity} left" for item in low_stock)

    @classmethod
    def get_inventory_summary(cls) -> List[str]:
        """
        Returns a summary of all inventory items in the system.

        The summary is a list of strings, each showing the product name, quantity, and location
        for every item in the inventory, in the format:
        "Product_Name Quantity at Location".

        Returns:
            list: A list of strings, each representing an inventory item.
        """
        return [f"{item.product_name} {item.quantity} at {item.location}" for item in cls.total_inventory]

# Test your class:
item1 = InventoryItem("Laptop", quantity=50, location="Warehouse A")
item2 = InventoryItem("Mouse", quantity=5, location="Warehouse B") 
item3 = InventoryItem("Keyboard", quantity=200, location="Warehouse A")

item1.update_quantity(-10)  # Sell 10 laptops
item2.update_quantity(-3)   # Sell 3 mice

print(item1.get_status())                    # Expected: status info
print(item2.is_low_stock())                  # Expected: True (only 2 left)
print(InventoryItem.get_low_stock_items())   # Expected: list of items needing reorder
print(InventoryItem.get_inventory_summary()) # Expected: system-wide summary

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We need to track inventory across our warehouses. Each product should know its 
stock level, location, and whether we need to reorder. The system should keep track of all products 
and tell us which ones are running low."

Developer Clarifications Asked:
- Should the system validate against predefined product/location catalogs?
- What constitutes "low stock" threshold?
- What status information is needed for operational decisions?

Stakeholder Responses:
- Yes, validate against business catalogs to prevent data entry errors
- Low stock threshold of 5 units works for our standard reordering process
- Status should show current quantity, location, and alert level for warehouse staff

Final Technical Decisions:
- Predefined PRODUCTS and LOCATIONS lists with validation
- Low stock threshold of 5 units (configurable via constant if needed)
- Dynamic low stock calculation to eliminate data consistency issues
- Single source of truth pattern using object references instead of duplicate data

Assumptions Documented:
- Each inventory item represents one product at one specific location
- Negative quantity updates represent sales/usage, positive represent restocking
- System prevents overselling (cannot reduce quantity below zero)
- Low stock alerts generated in real-time for immediate visibility
"""