def fib(n):
    if n == 1:
        return 1

    x1 = 1 
    x2 = 2 
    for _ in range(n-2):
        x1, x2 = x2, x1 + x2

    return x2

total = 0
for i in range(1, 1000):
    f = fib(i)
    if f >= 4000000:
        break
    if f % 2 == 0:
         total += f

print(total)

