import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def largest_prime(m):
    for j in range(2,int(m / 2)+1):
        q,r = divmod(m,j)
        if r == 0 and is_prime(q):
            return q

    return -1

print(largest_prime(600851475143))

