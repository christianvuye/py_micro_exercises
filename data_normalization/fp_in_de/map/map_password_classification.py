# type: ignore
"""
Password Strength Classification
Classify passwords as "weak", "medium", or "strong" based on length and character variety:
- Strong: 12+ chars with uppercase, lowercase, numbers, and symbols
- Medium: 8+ chars with at least 3 character types
- Weak: everything else
"""

passwords = [
    "password123",          # weak (no uppercase, no symbols)
    "MyPassword123!",       # strong (all criteria met)
    "short1!",              # weak (too short)
    "LongPassword123",      # medium (no symbols)
    "VerySecure2024!"       # strong (all criteria met)
]

# Expected output: ["weak", "strong", "weak", "medium", "strong"]

import re

strong_classification_pattern = re.compile(
    r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s]).{12,}$'
    )
medium_classification_pattern = re.compile(
    r'^(?=.{8,}$)'
    r'((?=.*[A-Z])(?=.*[a-z])(?=.*\d)'
    r'|(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])'
    r'|(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])'
    r'|(?=.*[a-z])(?=.*\d)(?=.*[^\w\s])).*$'
)

def password_strength_classifier(password):
    if re.match(strong_classification_pattern, password):
        return "strong"
    elif re.match(medium_classification_pattern, password):
        return "medium"
    else:
        return "weak"
    
password_classification = map(password_strength_classifier, passwords)

print(list(password_classification))
