# type: ignore
"""
Log Entry Parsing
Parse web server log entries to extract key metrics for monitoring dashboards:
"""

log_entries = [
    "2024-06-18 10:23:45 GET /api/users 200 0.045",
    "2024-06-18 10:24:12 POST /api/orders 201 0.234", 
    "2024-06-18 10:24:33 GET /api/products 404 0.012",
    "2024-06-18 10:25:01 PUT /api/users/123 500 1.205",
    "2024-06-18 10:25:15 GET /health 200 0.003"
]

# Expected output:
# [
#   {"timestamp": "2024-06-18 10:23:45", "method": "GET", "endpoint": "/api/users", "status": 200, "response_time": 0.045},
#   {"timestamp": "2024-06-18 10:24:12", "method": "POST", "endpoint": "/api/orders", "status": 201, "response_time": 0.234},
#   {"timestamp": "2024-06-18 10:24:33", "method": "GET", "endpoint": "/api/products", "status": 404, "response_time": 0.012},
#   {"timestamp": "2024-06-18 10:25:01", "method": "PUT", "endpoint": "/api/users/123", "status": 500, "response_time": 1.205},
#   {"timestamp": "2024-06-18 10:25:15", "method": "GET", "endpoint": "/health", "status": 200, "response_time": 0.003}
# ]

def extract_metrics(log_entry):
    extracted_metrics = {}
    log_entry_list = log_entry.split()
    extracted_metrics["timestamp"] = log_entry_list[0] + " " + log_entry_list[1]
    extracted_metrics["method"] = log_entry_list[2]
    extracted_metrics["endpoint"] = log_entry_list[3]
    extracted_metrics["status"] = int(log_entry_list[4])
    extracted_metrics["response_time"] = float(log_entry_list[5])
    return extracted_metrics

extracted_metrics_monitoring_dashboard = map(extract_metrics, log_entries)

for metrics in list(extracted_metrics_monitoring_dashboard):
    print(metrics)

