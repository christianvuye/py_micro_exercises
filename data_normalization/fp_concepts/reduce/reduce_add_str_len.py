# type: ignore

from functools import reduce

sum_str_len = reduce(lambda a,b: a + len(b), ["cat", "dog", "bird"], 0)

print(sum_str_len)