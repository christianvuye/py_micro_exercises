# type: ignore

from functools import reduce

concatenate_str = reduce(lambda x,y: x+ y, ["Hello", " ", "World"])

print(concatenate_str)