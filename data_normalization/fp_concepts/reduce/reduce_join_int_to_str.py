# type: ignore

from functools import reduce

join_int_to_str = reduce(lambda x,y:str(x)+str(y), [1, 2, 3, 4])

print(join_int_to_str)