# type: ignore

from functools import reduce

find_common_letters = reduce(lambda acc, current_string: [letter for letter in acc if letter in current_string], ["hello", "help", "hero"])

print(find_common_letters)