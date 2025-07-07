"""
You're building a configuration manager for a web application. Create a Config class 
that stores settings, validates them, and provides environment-specific overrides.

Your task: Create a Config class for application settings
Test with:
config = Config({"debug": True, "port": 8000})
print(config.get_setting("port"))  # Should print 8000
config.update_setting("port", 9000)
print(config.validate_settings())  # Should return True if all settings valid
"""

class Config:
    def __init__(self, settings):
        self.settings = settings
    
    def get_setting(self, setting):
        return self.settings[setting]

    def update_setting(self, setting, value):
        self.settings[setting] = value
    
    def validate_settings(self):
        return self.settings["port"] in range(1, 65536) and type(self.settings["debug"]) is bool
    
config = Config({"debug": True, "port": 8000})
print(config.get_setting("port"))  # Should print 8000
config.update_setting("port", 9000)
print(config.validate_settings())  # Should return True if all settings valid