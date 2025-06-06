# type: ignore

isdivisblebythree = map(lambda x: True if x % 3 == 0 else False, [3, 5, 6, 9])

print(list(isdivisblebythree))