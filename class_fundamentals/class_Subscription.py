"""
Create a Subscription class for a streaming service.

Requirements:
- Initialize with service_name, monthly_price, and active status (default: True)
- Create method cancel() that sets active to False and returns self
- Create method reactivate() that sets active to True and returns self  
- Create method change_price(new_price) that updates price and returns self
- Create method get_status() that returns a formatted string with all info

Test your class (note the chaining):
sub = Subscription("Netflix", 15.99)
result = sub.change_price(12.99).cancel().get_status()
print(result)  # Should show: "Netflix: $12.99/month (Inactive)"

sub.reactivate()
print(sub.get_status())  # Should show: "Netflix: $12.99/month (Active)"
"""

class Subscription:
    def __init__(self, service_name, monthly_price, active_status=True):
        self.service_name = service_name
        self.monthly_price = monthly_price
        self.active_status = active_status
    
    def cancel(self):
        self.active_status = False
        return self
    
    def reactivate(self):
        self.active_status = True
        return self

    def change_price(self, new_price):
        self.monthly_price = new_price
        return self
    
    def get_status(self):
        return f"{self.service_name}: ${self.monthly_price}/month ({"Active" if self.active_status else "Inactive"})"
    
sub = Subscription("Netflix", 15.99)
result = sub.change_price(12.99).cancel().get_status() # note the chaining, returning the instance allows you to keep calling methods on it
print(result)  # Should show: "Netflix: $12.99/month (Inactive)"

sub.reactivate()
print(sub.get_status())  # Should show: "Netflix: $12.99/month (Active)"