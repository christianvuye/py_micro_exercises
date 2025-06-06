# type: ignore

longerthanfourchars = filter(lambda x:len(x) > 4, ["cat", "dog", "elephant", "bird"])

print(list(longerthanfourchars))