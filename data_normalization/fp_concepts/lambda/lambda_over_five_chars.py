# type: ignore

over_five_chars = lambda x: True if len(x) > 5 else False

print(over_five_chars("Christian"))
print(over_five_chars("hi"))
print(over_five_chars("hello"))
