def find_triplet(n):
    for a in range(1,n):
        for b in range(1,n):
            if a * a + b * b == (n - b - a) * (n - b - a):
                return (a,b,n-a-b)

    return 'none'


def prod_triplet(n):
    total = 1
    for x in find_triplet(n):
        total = total * x

    return total

print(prod_triplet(1000))
