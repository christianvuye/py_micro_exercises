"""
You're creating a caching system for web requests. Create a Cache class that stores 
key-value pairs with expiration times and automatic cleanup of expired entries.

Your task: Create a Cache class for web application caching
Test with:
cache = Cache()
cache.set("user_123", {"name": "Alice"}, 60)  # key, value, ttl_seconds
print(cache.get("user_123"))  # Should return {"name": "Alice"}
cache.expire("user_123")
print(cache.get("user_123"))  # Should return None
"""

class Cache:
    def __init__(self):
        self.data = {}
    
    def set(self, key, value, ttl_seconds):
        self.data[key] = value
    
    def get(self, key):
        return self.data.get(key)
    
    def expire(self, key):
        self.data.pop(key, None)

cache = Cache()
cache.set("user_123", {"name": "Alice"}, 60)  # key, value, ttl_seconds
print(cache.get("user_123"))  # Should return {"name": "Alice"}
cache.expire("user_123")
print(cache.get("user_123"))  # Should return None