# type: ignore

from functools import reduce

sum_numbers = reduce(lambda x,y: x+ y, [1, 2, 3, 4, 5])

print(sum_numbers)