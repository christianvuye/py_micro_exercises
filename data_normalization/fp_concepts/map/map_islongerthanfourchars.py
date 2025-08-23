# type: ignore

islongerthanfourchars = map(
    lambda x: True if len(x) > 4 else False, ["cat", "elephant", "dog"]
)

print(list(islongerthanfourchars))
