"""
You're building a JSON API response formatter. Create a Response class that formats 
data into standard API responses with status codes, messages, and pagination info.

Your task: Create a Response class for API standardization
Test with:
response = Response(200, "success", {"users": ["Alice", "Bob"]})
print(response.to_json())  # Should return formatted JSON string
response.add_pagination(1, 10, 25)  # page, per_page, total
print(response.get_status())  # Should return 200
"""

import json, math

class Response:
    def __init__(self, status_code, message, data):
        self.status_code = status_code              # HTTP status (200=success, 404=not found, etc.)
        self.message = message                      # Human-readable message ("success", "error", etc.)
        self.data = data                            # The actual content (users, products, whatever)
        self.pagination = None                      # Will store pagination info when added
    
    def to_json(self):
        response_dict = {
                "status":self.status_code, 
                "message":self.message, 
                "data":self.data,
            }
        
        if self.pagination is not None:
            response_dict["pagination"] = self.pagination

        return json.dumps(response_dict)

    def get_status(self):
        return self.status_code

    def add_pagination(self, page, per_page, total):
        total_pages = math.ceil(total/per_page)

        self.pagination = {
            "page": page,                           # Current page number
            "per_page": per_page,                   # Items shown per page     
            "total": total,                         # Total items in collection
            "total_pages": total_pages              # Total pages needed
        }

response = Response(200, "success", {"users": ["Alice", "Bob"]})
print(response.to_json())  # Should return formatted JSON string
response.add_pagination(1, 10, 25)  # page, per_page, total
print(response.get_status())  # Should return 200