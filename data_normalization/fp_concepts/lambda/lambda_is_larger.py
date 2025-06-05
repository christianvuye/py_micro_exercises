# type: ignore

is_larger = lambda a,b: a if a > b else b if b > a else "equal"

print(is_larger(2,4))
print(is_larger(8,2))
print(is_larger(6,6))