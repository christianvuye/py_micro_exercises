"""
Create a ConfigManager class that demonstrates attribute shadowing.

Requirements:
- Class variable default_timeout = 30
- Class variable debug_mode = False
- NO instance variables in __init__ - start with empty instances

Create methods:
- set_timeout(value) that sets timeout for this instance
- get_timeout() that returns timeout (instance or class default)
- enable_debug() that sets debug_mode for this instance
- get_debug_status() that returns debug status
- Class method set_global_timeout(value) that changes default for all

Tricky test scenario:
config1 = ConfigManager()
config2 = ConfigManager()

print(f"Initial timeouts - Config1: {config1.get_timeout()}, Config2: {config2.get_timeout()}")

config1.set_timeout(60)
print(f"After config1 change - Config1: {config1.get_timeout()}, Config2: {config2.get_timeout()}")

ConfigManager.set_global_timeout(90)
print(f"After global change - Config1: {config1.get_timeout()}, Config2: {config2.get_timeout()}")

# The shocking part:
print(f"Config1 default_timeout: {config1.default_timeout}")
print(f"Config2 default_timeout: {config2.default_timeout}")
print(f"Class default_timeout: {ConfigManager.default_timeout}")
"""


class ConfigManager:
    default_timeout = 30
    debug_mode = False

    # __init__ methods in Python always implicitly return None. 
    # You should never return self from __init__; it would cause a TypeError
    def __init__(self): # 
        pass 

    def set_timeout(self, value):
        self.custom_instance_timeout = value
    
    def get_timeout(self):
        return getattr(self, "custom_instance_timeout", ConfigManager.default_timeout)
    
    def enable_debug(self):
        self.debug_mode_instance = True

    def get_debug_status(self):
        return getattr(self, "debug_mode_instance", ConfigManager.debug_mode)    
    
    @classmethod
    def set_global_timeout(cls, value):
        cls.default_timeout = value


config1 = ConfigManager()
config2 = ConfigManager()

print(f"Initial timeouts - Config1: {config1.get_timeout()}, Config2: {config2.get_timeout()}")

config1.set_timeout(60)
print(f"After config1 change - Config1: {config1.get_timeout()}, Config2: {config2.get_timeout()}")

ConfigManager.set_global_timeout(90)
print(f"After global change - Config1: {config1.get_timeout()}, Config2: {config2.get_timeout()}")

# The shocking part:
print(f"Config1 default_timeout: {config1.default_timeout}")
print(f"Config2 default_timeout: {config2.default_timeout}")
print(f"Class default_timeout: {ConfigManager.default_timeout}")