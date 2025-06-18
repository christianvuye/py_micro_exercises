# type: ignore
"""
URL Slug Generation
Convert article titles to URL-friendly slugs (lowercase, spaces to hyphens, remove special chars):
"""

article_titles = [
    "How to Learn Python Programming!",
    "Data Science 101: A Beginner's Guide",
    "Machine Learning & AI Trends",
    "The Future of Work (2024 Edition)"
]

# Expected output: 
# ["how-to-learn-python-programming", "data-science-101-a-beginners-guide", "machine-learning-ai-trends", "the-future-of-work-2024-edition"]
    
url_slug = map(lambda x:x.lower().replace(" ", "-",).replace("!", "").replace(":","").replace("&", "").replace("(","").replace(")","").replace("--", "-").replace("'", ""), article_titles)

print(list(url_slug))

import re

def to_url_slug(article_title):
    url_slug = article_title.lower().replace(" ", "-")
    url_slug = re.sub(r'[^a-zA-Z0-9-]', '', url_slug)
    url_slug = url_slug.replace("--", "-")
    return url_slug

url_slug = map(to_url_slug, article_titles)

print(list(url_slug))

# Real-world production improvements
def to_url_slug_improved(title):
    slug = re.sub(r'[^\w\s-]', '', title.lower())   # Remove special chars
    slug = re.sub(r'[-\s]+', '-', slug)             # Replace spaces/multiple hyphens
    return slug.strip('-')                          # Remove leading/trailing hyphens 

url_slug = map(to_url_slug_improved, article_titles)

print(list(url_slug))
