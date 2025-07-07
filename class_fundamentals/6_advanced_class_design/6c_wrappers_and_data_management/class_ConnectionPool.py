"""
You're developing a database connection pool manager. Create a ConnectionPool class 
that manages active connections, enforces limits, and tracks usage statistics.

Your task: Create a ConnectionPool class for database management
Test with:
pool = ConnectionPool(max_connections=5)
conn1 = pool.get_connection()
print(pool.active_connections())  # Should print 1
pool.release_connection(conn1)
print(pool.active_connections())  # Should print 0
"""

class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.active_count = 0

    def get_connection(self):
        if self.active_count < self.max_connections:
            self.active_count += 1
            return f"conn_{self.active_count}"
        else:
            return None

    def release_connection(self, connection):
        if self.active_count > 0:
            self.active_count -= 1

    def active_connections(self):
        return self.active_count

pool = ConnectionPool(max_connections=5)
conn1 = pool.get_connection()
print(pool.active_connections())  # Should print 1
pool.release_connection(conn1)
print(pool.active_connections())  # Should print 0