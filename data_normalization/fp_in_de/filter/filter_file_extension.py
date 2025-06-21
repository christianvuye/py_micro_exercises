"""
File Extension Filtering
Filter uploaded files to only allow supported formats before processing in data pipeline:
"""

uploaded_files = [
    {"filename": "sales_data.csv", "size": 1024000, "upload_time": "2024-06-21 10:30:00"},
    {"filename": "customer_report.xlsx", "size": 2048000, "upload_time": "2024-06-21 10:31:00"},
    {"filename": "malware.exe", "size": 512000, "upload_time": "2024-06-21 10:32:00"},
    {"filename": "inventory.json", "size": 256000, "upload_time": "2024-06-21 10:33:00"},
    {"filename": "backup.zip", "size": 5120000, "upload_time": "2024-06-21 10:34:00"},
    {"filename": "user_data.parquet", "size": 3072000, "upload_time": "2024-06-21 10:35:00"},
    {"filename": "system.log", "size": 128000, "upload_time": "2024-06-21 10:36:00"},
    {"filename": "analytics.txt", "size": 64000, "upload_time": "2024-06-21 10:37:00"},
    {"filename": "config.xml", "size": 32000, "upload_time": "2024-06-21 10:38:00"}
]

# Allowed file extensions for data processing
ALLOWED_EXTENSIONS = {".csv", ".xlsx", ".json", ".parquet", ".xml"}

# Expected output: Files with extensions in ALLOWED_EXTENSIONS
# Should return: sales_data.csv, customer_report.xlsx, inventory.json, user_data.parquet, config.xml

from os.path import splitext

# Method 1 (splitext): More explicit, clearer intent, better for debugging, handles edge cases
def file_extension_allowed(uploaded_file_details: dict) -> bool:
    filename, extension = splitext(uploaded_file_details["filename"])
    return extension in ALLOWED_EXTENSIONS

# Method 2 (endswith): More concise, slightly faster (no string splitting)
def file_extension_allowed_tuple(uploaded_file_details: dict) -> bool:
    return uploaded_file_details["filename"].endswith(tuple(ALLOWED_EXTENSIONS))

allowed_uploaded_files = filter(file_extension_allowed, uploaded_files)
print(*(file_detail["filename"] for file_detail in list(allowed_uploaded_files)), sep=", ")

allowed_uploaded_files_tuple = filter(file_extension_allowed_tuple, uploaded_files)
print(*(file_detail["filename"] for file_detail in list(allowed_uploaded_files_tuple)), sep=", ")