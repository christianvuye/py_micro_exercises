# type: ignore

from math import gcd
from functools import reduce

find_gcd = reduce(lambda x,y: gcd(x,y), [12, 8, 16])

print(find_gcd)