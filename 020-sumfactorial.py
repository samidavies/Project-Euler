prod = 1
for i in range(2,101):
    prod *= i
addable = str(prod)
print(sum(int(a) for a in addable))
