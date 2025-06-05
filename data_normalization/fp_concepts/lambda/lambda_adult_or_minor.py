# type: ignore

adult_or_minor = lambda x: "adult" if x >= 18 else "minor"

print(adult_or_minor(15))
print(adult_or_minor(25))
print((adult_or_minor(18)))