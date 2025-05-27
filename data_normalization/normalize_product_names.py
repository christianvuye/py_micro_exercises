# Define dictionary here once, so the dictionary does not need to be created every time it gets called
SUFFIX_REPLACEMENTS = {
    "Corporation": "Corp",
    "Incorporated": "Inc", 
    "Inc.": "Inc"
}

def normalize_product_names(data: list[str]) -> list[str]:
    normalized_product_names: list[str] = []
    for product_name in data:
        product_name_cleaned = product_name.strip().title()
        for original, replacement in SUFFIX_REPLACEMENTS.items():
            if original in product_name_cleaned:
                product_name_cleaned = product_name_cleaned.replace(original, replacement)
        if len(product_name_cleaned) >= 2:
            normalized_product_names.append(product_name_cleaned)
    return normalized_product_names