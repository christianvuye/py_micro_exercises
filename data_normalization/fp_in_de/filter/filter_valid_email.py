"""
Valid Email Filtering
Filter out invalid email addresses from customer registration data:
"""

customer_emails = [
    "john.doe@company.com",
    "invalid-email", 
    "jane@domain.co.uk",
    "broken@email",
    "admin@site.org",
    "@missing-local.com",
    "user@domain.info",
    "no-at-symbol.com",
    "test@valid-domain.net"
]

# Expected output: ["john.doe@company.com", "jane@domain.co.uk", "admin@site.org", "user@domain.info", "test@valid-domain.net"]

from re import compile, fullmatch

email_pattern = compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def validate_email(email: str) -> bool:
    return bool(fullmatch(email_pattern, email))

validated_emails = filter(validate_email, customer_emails)

print(list(validated_emails))