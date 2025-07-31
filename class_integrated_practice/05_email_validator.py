"""
Build an email validation service that processes bulk email lists and provides detailed validation reports.

Concepts practiced:
- Static methods only (no instance state needed)
- Bulk operations (processing lists and collections)
- Validation patterns (regex, business rules, data quality)

Business Requirements:
- Validate email addresses against business standards
- Process large batches of emails efficiently  
- Generate detailed validation reports with error categories
- Support different validation strictness levels
- Provide statistics on validation results

Your stakeholder says: "We import customer email lists from various sources - spreadsheets, 
APIs, forms. The data quality is inconsistent. We need a validator that can process thousands 
of emails and tell us what's wrong with the bad ones. Some campaigns need strict validation, 
others can be more lenient."

# Test your class:
emails = [
    "valid@example.com",
    "invalid.email",
    "user@domain",
    "test@valid-site.org",
    "",
    "admin@company.co.uk"
]

valid_emails = EmailValidator.validate_batch(emails)
report = EmailValidator.generate_report(emails)
strict_valid = EmailValidator.validate_batch(emails, strict=True)

print(len(valid_emails))                    # Expected: count of valid emails
print(EmailValidator.is_valid("test@example.com"))  # Expected: True/False
print(report)                               # Expected: detailed validation report
"""

from typing import List
from re import compile, fullmatch

class EmailValidator:
    """
    Utility class for validating and categorizing email addresses.
    All methods are static; no instance state is used.
    """

    pattern_lenient = compile(
        r"^[A-Za-z0-9._%+-]+"
        r"@"
        r"[A-Za-z0-9.-]+\."
        r"[A-Za-z]{2,}$"
    )

    pattern_strict = compile(
        r"^[a-zA-Z0-9][a-zA-Z0-9._%+-]*[a-zA-Z0-9]"
        r"@"
        r"[a-zA-Z0-9][a-zA-Z0-9.-]*[a-zA-Z0-9]"
        r"\."
        r"[a-zA-Z]{2,4}$"
    )

    pattern_typos = compile(
        r".*@@.*"
        r"|.*\.\..*"
        r"|.*@g[mn]?[ai]*l\.(co[mn]?|ne[tw]?)$"
        r"|.*@ya[hk]?oo?\.(co[mn]?|ne[tw]?)$"
        r"|.*@h[ou]tm[ai][il]l?\.(co[mn]?|ne[tw]?)$"
    )

    pattern_missing_parts = compile(
        r"^$"
        r"|^\s*$"
        r"|^[^@]*\.[a-z]{2,}$"
        r"|.*@[^.]*$"
        r"|.*@$"
        r"|^@.*$"
        r"|^@$"
    )

    pattern_wrong_formatting = compile(
        r"^\.|\.@"
        r"|.*\.$"
        r"|\.\."
        r"|.*@.*@.*$"
        r"|^@"
        r"|@$"
        r"|.*@-.*$"
        r"|.*@.*-\..*$"
        r"|.*@.*--.*$"
        r"|.*\.[0-9]"
    )

    pattern_invalid_chars = compile(
        r'[<>()[\]\\,;:\s@"]'
        r'|.*@.*[^a-zA-Z0-9.-].*$'
        r'|.*@.*_.*$'
        r'|[^\x00-\x7F]'
    )

    pattern_violate_bizrules = compile(
        r".*@(10minutemail|tempmail|guerrillamail|mailinator|throwaway)\..*"
        r"|.*@(g00gle|micr0soft|fac3book)\..*"
        r"|.*\.(tk|ml|ga|cf)$"
        r"|.*@(gmail|yahoo|hotmail|outlook|aol)\..*"
        r"|^.*[0-9].*@.*$"
        r"|^.{0,5}@.*$"
        r"|^.*@.{0,3}$"
    )

    @staticmethod
    def validate_batch(emails: List[str], strict: bool = False) -> List[str]:
        """
        Validate a batch of email addresses.

        Args:
            emails (List[str]): List of email address strings to validate.
            strict (bool, optional): Use strict validation rules if True, else lenient. Defaults to False.

        Returns:
            List[str]: Valid email addresses from the input list, according to the selected rules.
        """
        pattern = EmailValidator.pattern_strict if strict else EmailValidator.pattern_lenient
        return [e for e in emails if isinstance(e, str) and fullmatch(pattern, e)]

    @staticmethod
    def is_valid(email: str, strict: bool = False) -> bool:
        """
        Validates whether the provided email address is in a correct format.

        Args:
            email (str): The email address to validate.
            strict (bool, optional): If True, uses a stricter validation pattern. 
                If False, uses a more lenient pattern. Defaults to False.

        Returns:
            bool: True if the email address is valid according to the selected pattern, False otherwise.
        """
        pattern = EmailValidator.pattern_strict if strict else EmailValidator.pattern_lenient
        return isinstance(email, str) and bool(fullmatch(pattern, email))

    @staticmethod
    def categorize_batch(emails: List[str]) -> dict:
        """
        Categorizes a batch of email addresses based on validation and error type.

        Args:
            emails (List[str]): A list of email addresses to be categorized.

        Returns:
            dict: A dictionary with the following keys, each mapping to a list of emails that fall into that category:
            - "wrong_type": Emails that are not of type `str`.
            - "valid_strict": Emails that strictly match the most rigorous validation pattern.
            - "valid_lenient": Emails that match a more lenient validation pattern.
            - "typos": Emails that match common typo patterns.
            - "missing_parts": Emails missing required parts (e.g., missing '@' or domain).
            - "wrong_formatting": Emails with formatting issues.
            - "invalid_chars": Emails containing invalid characters.
            - "violate_bizrules": Emails that violate business-specific rules.
            - "other_violation": Emails that do not fit any of the above categories.
        """
        cats = {
            "wrong_type": [], "valid_strict": [], "valid_lenient": [],
            "typos": [], "missing_parts": [], "wrong_formatting": [],
            "invalid_chars": [], "violate_bizrules": [], "other_violation": []
        }
        for email in emails:
            if not isinstance(email, str):
                cats["wrong_type"].append(email)
            elif fullmatch(EmailValidator.pattern_strict, email):
                cats["valid_strict"].append(email)
            elif fullmatch(EmailValidator.pattern_lenient, email):
                cats["valid_lenient"].append(email)
            elif fullmatch(EmailValidator.pattern_typos, email):
                cats["typos"].append(email)
            elif fullmatch(EmailValidator.pattern_missing_parts, email):
                cats["missing_parts"].append(email)
            elif fullmatch(EmailValidator.pattern_wrong_formatting, email):
                cats["wrong_formatting"].append(email)
            elif fullmatch(EmailValidator.pattern_invalid_chars, email):
                cats["invalid_chars"].append(email)
            elif fullmatch(EmailValidator.pattern_violate_bizrules, email):
                cats["violate_bizrules"].append(email)
            else:
                cats["other_violation"].append(email)
        return cats

    @staticmethod
    def generate_report(emails: List[str]) -> str:
        """
        Generates a summary report of email validation results.

        Args:
            emails (List[str]): A list of email addresses to validate and summarize.

        Returns:
            str: A formatted string report summarizing the validation results, including counts for each validation category:
                - Total processed
                - Valid (strict)
                - Valid (lenient)
                - Wrong type
                - Typos
                - Missing parts
                - Wrong formatting
                - Invalid characters
                - Violates business rules
                - Other violations

        """
        c = EmailValidator.categorize_batch(emails)
        total = len(emails)
        def pct(n):
            return f"{(n/total*100):5.1f}%" if total else "0.0%"
        return (
            "Email Validation Report:\n"
            f"  Total processed:       {total}\n"
            f"  Valid (strict):        {len(c['valid_strict']):3d}  ({pct(len(c['valid_strict']))})\n"
            f"  Valid (lenient):       {len(c['valid_lenient']):3d}  ({pct(len(c['valid_lenient']))})\n"
            f"  Wrong type:            {len(c['wrong_type']):3d}  ({pct(len(c['wrong_type']))})\n"
            f"  Typos:                 {len(c['typos']):3d}  ({pct(len(c['typos']))})\n"
            f"  Missing parts:         {len(c['missing_parts']):3d}  ({pct(len(c['missing_parts']))})\n"
            f"  Wrong formatting:      {len(c['wrong_formatting']):3d}  ({pct(len(c['wrong_formatting']))})\n"
            f"  Invalid characters:    {len(c['invalid_chars']):3d}  ({pct(len(c['invalid_chars']))})\n"
            f"  Violates biz rules:    {len(c['violate_bizrules']):3d}  ({pct(len(c['violate_bizrules']))})\n"
            f"  Other violations:      {len(c['other_violation']):3d}  ({pct(len(c['other_violation']))})"
        )

# Test your class:
emails = [
    "valid@example.com",
    "invalid.email",
    "user@domain",
    "test@valid-site.org",
    "",
    "admin@company.co.uk"
]

valid_emails = EmailValidator.validate_batch(emails)
report = EmailValidator.generate_report(emails)
strict_valid = EmailValidator.validate_batch(emails, strict=True)

print(len(valid_emails))                    # Expected: count of valid emails
print(EmailValidator.is_valid("test@example.com"))  # Expected: True/False
print(report)                               # Expected: detailed validation report

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We need a validator that can process thousands of emails and tell us what's 
wrong with the bad ones. Some campaigns need strict validation, others can be more lenient."

Developer Clarifications Asked:
- What constitutes "strict" vs "lenient" validation standards?
- Which error categories would provide actionable insights for list cleaning?
- Should business rules block specific types of email providers?

Stakeholder Responses:
- Strict validation for financial/legal contexts, lenient for marketing signups
- Marketing team needs to distinguish fixable errors (typos) from unfixable ones (missing parts)
- Yes, block temporary email services and suspicious domains for data quality

Final Technical Decisions:
- Two-tier validation: strict pattern (business context) vs lenient (marketing)
- Nine error categories prioritized by actionability and business value
- Business rule validation to block low-quality email sources
- Comprehensive reporting with percentages for data-driven list management

Assumptions Documented:
- Static methods only (no instance state needed for utility operations)
- Regex-based validation for performance with bulk processing
- Priority categorization (valid emails checked first, then specific error types)
- Formatted reporting suitable for both technical and business stakeholders
"""