# type: ignore

from functools import reduce

product_even_nrs = reduce(lambda acc,y: acc*y if y % 2==0 else acc, [2, 3, 4, 5, 6], 1)

print(product_even_nrs)