"""
Create a class called `Product` with class variable `tax_rate = 0.08` and instance variables 
`name` and `price`. Add a method `total_price` that returns price including tax.

Your task: Define Product class with class and instance variables
Test it with:
product = Product("Laptop", 1000)
print(product.total_price())  # Should print 1080.0
"""

class Product:
    tax_rate = 0.08

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def total_price(self):
        return self.price + (self.price * Product.tax_rate)

product = Product("Laptop", 1000)
print(product.total_price())  # Should print 1080.0