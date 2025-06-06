# type: ignore

palindromes = filter(lambda x: x == x[::-1], ["level", "hello", "radar", "world"])

print(list(palindromes))