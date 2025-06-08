# type: ignore

from functools import reduce

factorial = reduce(lambda a,b: a * b, [1, 2, 3, 4])

print(factorial)