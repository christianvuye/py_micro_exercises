# type: ignore

str_not_empty = filter(lambda x:len(x) != 0, [1, 3, 5, 6, 9, 12, 15, 18])

print(list(str_not_empty))