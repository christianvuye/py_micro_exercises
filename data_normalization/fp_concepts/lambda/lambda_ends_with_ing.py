# type: ignore

ends_with_ing = lambda x: True if x.endswith("ing") else False

print(ends_with_ing("ing"))
print(ends_with_ing("morning"))
print(ends_with_ing("growing"))
print(ends_with_ing("moving"))
print(ends_with_ing("meh"))