from re import fullmatch

def normalize_emails(data: list[str]) -> list[str]:
    normalized_emails: list[str] = []
    email_pattern = "^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$" # type: ignore
    for email in data:
        email_cleaned = email.strip().lower()
        if fullmatch(email_pattern, email_cleaned):
            normalized_emails.append(email_cleaned)
    return normalized_emails