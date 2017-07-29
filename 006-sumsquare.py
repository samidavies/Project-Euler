def sum_square(n):
    return sum(i*i for i in range(1, n+1))

def square_sum(m):
    return sum(i for i in range(1, m+1)) ** 2

print(square_sum(100) - sum_square(100))

