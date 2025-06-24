from requests import Session, HTTPError, RequestException

class APIClient:
    def __init__(self, base_url, auth_token=None):
        """
        Initialize the API client with base URL and optional authentication.
        
        Args:
            base_url: Root URL for the API (e.g., "https://api.github.com")
            auth_token: Optional authentication token
        """
        # Store the base URL, removing trailing slash for consistency
        self.base_url = base_url.rstrip('/')
        
        # Store authentication token
        self.auth_token = auth_token
        
        # creates a new session manager object to make HTTP requests, an empty container for session info, check definition for available methods
        self.session = Session()
        
        # Set up authentication headers if token provided
        if self.auth_token:
            self.session.headers.update({
                'Authorization': f'Bearer {self.auth_token}'
            })
    
    def get(self, endpoint):
        """
        Make a GET request to the specified endpoint.
        
        Args:
            endpoint: The API endpoint (e.g., "/users/1")
            
        Returns:
            dict: The JSON response data
        """
        full_url = self.base_url + endpoint

        try:
            response = self.session.get(full_url)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return None
        except RequestException as e:
            print(f"RequestException error occurred: {e}")
            return None
        except Exception as e:
            print(f"Another exception was raised: {e}")
            return None

    def post(self, endpoint, data=None):
        """
        Make a POST request to the specified endpoint.
        
        Args:
            endpoint: The API endpoint (e.g., "/users")
            data: Dictionary of data to send in request body
            
        Returns:
            dict: The JSON response data
        """
        full_url = self.base_url + endpoint

        try:
            response = self.session.post(full_url, json=data)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return None
        except RequestException as e:
            print(f"RequestException error occurred: {e}")
            return None
        except Exception as e:
            print(f"Another exception was raised: {e}")
            return None

client = APIClient("https://jsonplaceholder.typicode.com")
user_data = client.get("/users/1")
print(user_data.get("name"))  # Should print a real name! #type: ignore

# Create a new user
new_user = {
    "name": "John Doe",
    "email": "john@example.com"
}
result = client.post("/users", data=new_user)
print(result)

# Test both methods
client = APIClient("https://jsonplaceholder.typicode.com")

# Test GET
user_data = client.get("/users/1")
print(f"User name: {user_data.get('name') if user_data else 'Failed'}")

# Test POST  
new_user = {
    "name": "John Doe", 
    "email": "john@example.com"
}
result = client.post("/users", data=new_user)
print(f"Created user ID: {result.get('id') if result else 'Failed'}")