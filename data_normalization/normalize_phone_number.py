from re import compile

def normalize_phone_numbers(data: list[str]) -> list[str]:
    normalized_phone_numbers: list[str] = []
    _non_digit_re = compile(r"\D")
    for phone_number in data:
        if phone_number.startswith("+1"):
            phone_number = phone_number.replace("+1", "", 1)
        phone_number_cleaned = _non_digit_re.sub("", phone_number)
        if len(phone_number_cleaned) == 10:
            normalized_phone_numbers.append(phone_number_cleaned)
    return normalized_phone_numbers