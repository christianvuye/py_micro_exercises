"""
You're building a file backup system. Create a FileBackup class that tracks file 
information, calculates checksums, and manages backup versions.

Your task: Create a FileBackup class for backup management
Test with:
backup = FileBackup("config.txt", 1024, "abc123")
print(backup.get_file_info())  # Should return formatted file details
print(backup.needs_backup("def456"))  # Should print True (checksum changed)
"""

class FileBackup:
    def __init__(self, filename, file_size, checksum):
        self.filename = filename
        self.file_size = file_size
        self.checksum = checksum

    def get_file_info(self):
        return f"{self.filename} ({self.file_size} bytes, checksum {self.checksum})"
    
    def needs_backup(self, checksum):
        return checksum != self.checksum
    

backup = FileBackup("config.txt", 1024, "abc123")
print(backup.get_file_info())  # Should return formatted file details
print(backup.needs_backup("def456"))  # Should print True (checksum changed)