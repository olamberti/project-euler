# Sum of mulitples of 3:
sum3 = sum([x for x in range(3, 1000, 3)])

# Sum of mulitples of 5:
sum5 = sum([x for x in range(5, 1000, 5)])

# Sum of mulitples of 15:
sum15 = sum([x for x in range(15, 1000, 15)])

# Add up the sums of 3 & 5 and subtract 15:
print(sum3 + sum5 - sum15)