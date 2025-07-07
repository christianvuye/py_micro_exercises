"""
You're creating a log analyzer for server monitoring. Create a LogEntry class that 
parses log lines, categorizes severity levels, and tracks error patterns.

Your task: Create a LogEntry class for log analysis
Test with:
log = LogEntry("2024-06-23 10:30:45 ERROR Database connection failed")
print(log.get_severity())  # Should print "ERROR"
print(log.is_error())      # Should print True
"""

class LogEntry:
    def __init__(self, log_line):
        self.log_line = log_line
        self.parts = log_line.split()
    
    def get_severity(self):
        return self.parts[2] # feels very fragile, as it is hardcoded, there must be a better solution
    
    def is_error(self):
        return self.get_severity() in ["ERROR", "FATAL"]

log = LogEntry("2024-06-23 10:30:45 ERROR Database connection failed")
print(log.get_severity())  # Should print "ERROR"
print(log.is_error())      # Should print True

log2 = LogEntry("2024-06-23 10:30:45 FATAL Database connection failed")
print(log2.get_severity())  # Should print "ERROR"
print(log2.is_error())      # Should print True