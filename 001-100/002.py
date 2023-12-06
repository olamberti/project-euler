# First two even terms of the Fibonacci sequence are
f1, f2 = 2, 8

result = f1
# Since every third term is even, it is enough to calculate them:
limit = 4_000_000
while f2  < 4_000_000:
    result += f2
    f1, f2 = f2, 4 * f2 + f1

print(result)