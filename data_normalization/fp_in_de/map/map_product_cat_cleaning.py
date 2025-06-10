# type: ignore
"""
Product Category Cleaning
Remove extra leading and trailing whitespace and convert to title case for product categories:
"""

raw_categories = [" electronics ", "HOME & garden", "  BOOKS   ", "clothing&accessories"]

raw_categories_cleaned = map(lambda x:x.strip().title(), raw_categories)

print(list(raw_categories_cleaned))