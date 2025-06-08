# type: ignore

from functools import reduce

merge_lists = reduce(lambda x,y:x+y, [[1, 2], [3, 4], [5, 6]])

print(merge_lists)