# type: ignore

greaterthanfiveandeven = filter(lambda x: x > 5 and x % 2 == 0, [2, 6, 3, 8, 5, 10])

print(list(greaterthanfiveandeven))