def gcd(a,b):
    if b > a:
        a, b = b, a
    r = a % b
    if r > 0:
        return gcd(b,r)
    return b

assert gcd(24,9) == 3
assert gcd(9,24) == 3
assert gcd(7,24) == 1

def lcm(a,b):
    return a * b / gcd(a,b)

def first_primes(n):
    primes = [2]
    check = 2
    while len(primes) < n:
        check += 1
        if all(check % p != 0 for p in primes):
            primes.append(check) 

    return primes

def primes_below(n):
    primes = [2]
    if n < 2:
        return []
    for i in range(2,n):
        if all(i % p != 0 for p in primes):
            primes.append(i)

    return primes


