# Sum function for x
def calc_sum(x):
    n = 999 // x
    return (x * n * (n + 1)) // 2

# Add up the sums of 3 & 5 and subtract 15:
print(calc_sum(3) + calc_sum(5) - calc_sum(15))