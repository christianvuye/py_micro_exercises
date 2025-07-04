"""
Create a Computer class that manages hardware components.

Requirements:
- Initialize with brand, processor_model, ram_gb, storage_gb
- Create method get_specs() that returns technical specs string
- Create method upgrade_ram(additional_gb) that increases RAM
- Create method upgrade_storage(additional_gb) that increases storage  
- Create method is_gaming_ready() that returns True if RAM >= 16GB and storage >= 500GB
- Create method get_summary() that returns user-friendly summary including gaming status

Example outputs:
get_specs(): "Intel i7, 16GB RAM, 500GB Storage"
get_summary(): "Dell Computer: Intel i7, 16GB RAM, 500GB Storage - Gaming Ready"
"""

class Computer:
    def __init__(self, brand, processor_model, ram_gb, storage_gb):
        self.brand = brand
        self.processor_model = processor_model
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
    
    def get_specs(self):
        return f"{self.processor_model}, {self.ram_gb}GB RAM, {self.storage_gb}GB Storage"
    
    def upgrade_ram(self, additional_gb):
        self.ram_gb += additional_gb
    
    def upgrade_storage(self, additional_gb):
        self.storage_gb += additional_gb
    
    def is_gaming_ready(self):
        return self.ram_gb >= 16 and self.storage_gb >= 500

    def get_summary(self):
        gaming_status = "Gaming Ready" if self.is_gaming_ready() else "Not Gaming Ready"
        return f"{self.brand} Computer: {self.get_specs()} - {gaming_status}"

# Test Case 1: Basic Initialization
print("=== Test Case 1: Basic Initialization ===")
pc1 = Computer("HP", "AMD Ryzen 5", 4, 128)
print(f"Initial specs: {pc1.get_specs()}")
print(f"Gaming ready: {pc1.is_gaming_ready()}")  # Should be False
print(f"Summary: {pc1.get_summary()}")
print()

# Test Case 2: Minimal Gaming Requirements
print("=== Test Case 2: Minimal Gaming Requirements ===")
pc2 = Computer("ASUS", "Intel i5", 16, 500)
print(f"Gaming ready: {pc2.is_gaming_ready()}")  # Should be True
print(f"Summary: {pc2.get_summary()}")
print()

# Test Case 3: RAM Upgrade Only
print("=== Test Case 3: RAM Upgrade Only ===")
pc3 = Computer("Lenovo", "Intel i7", 8, 256)
print(f"Before RAM upgrade: {pc3.is_gaming_ready()}")  # False
pc3.upgrade_ram(8)
print(f"After RAM upgrade: {pc3.get_specs()}")
print(f"Gaming ready after RAM: {pc3.is_gaming_ready()}")  # Still False (storage too low)
print()

# Test Case 4: Storage Upgrade Only
print("=== Test Case 4: Storage Upgrade Only ===")
pc4 = Computer("Dell", "Intel i9", 8, 250)
print(f"Before storage upgrade: {pc4.is_gaming_ready()}")  # False
pc4.upgrade_storage(300)
print(f"After storage upgrade: {pc4.get_specs()}")
print(f"Gaming ready after storage: {pc4.is_gaming_ready()}")  # Still False (RAM too low)
print()

# Test Case 5: Both Upgrades - Becomes Gaming Ready
print("=== Test Case 5: Both Upgrades - Becomes Gaming Ready ===")
pc5 = Computer("MSI", "AMD Ryzen 7", 12, 400)
print(f"Initial: {pc5.is_gaming_ready()}")  # False
pc5.upgrade_ram(4)   # 12 + 4 = 16GB
pc5.upgrade_storage(100)  # 400 + 100 = 500GB
print(f"Final specs: {pc5.get_specs()}")
print(f"Gaming ready: {pc5.is_gaming_ready()}")  # True
print(f"Summary: {pc5.get_summary()}")
print()

# Test Case 6: Already High-End Gaming PC
print("=== Test Case 6: Already High-End Gaming PC ===")
pc6 = Computer("Alienware", "Intel i9", 32, 1000)
print(f"High-end gaming ready: {pc6.is_gaming_ready()}")  # True
print(f"Summary: {pc6.get_summary()}")
print()

# Test Case 7: Edge Cases - Zero Upgrades
print("=== Test Case 7: Edge Cases - Zero Upgrades ===")
pc7 = Computer("Custom", "Intel i3", 8, 256)
pc7.upgrade_ram(0)  # Should not change anything
pc7.upgrade_storage(0)  # Should not change anything
print(f"After zero upgrades: {pc7.get_specs()}")  # Should be unchanged
print()

# Test Case 8: Large Upgrades
print("=== Test Case 8: Large Upgrades ===")
pc8 = Computer("Origin", "Intel i7", 8, 256)
pc8.upgrade_ram(56)   # 8 + 56 = 64GB
pc8.upgrade_storage(1744)  # 256 + 1744 = 2000GB
print(f"After massive upgrades: {pc8.get_specs()}")
print(f"Definitely gaming ready: {pc8.is_gaming_ready()}")  # True
print(f"Summary: {pc8.get_summary()}")