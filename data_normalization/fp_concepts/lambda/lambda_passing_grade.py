# type: ignore

pass_or_fail = lambda x: "pass" if x >= 60 else "fail"

print(pass_or_fail(60))
print(pass_or_fail(50))
print(pass_or_fail(65))