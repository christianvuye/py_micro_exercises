# type: ignore

from functools import reduce

max_value = reduce(lambda x,y: max(x,y), [3, 7, 2, 9, 1, 5])

print(max_value)