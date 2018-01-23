import math
from bisect import bisect_left

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



def divisors(n):
    result = set()
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            result.add(i)
            result.add(n/i)
    return result



def sieve(n):
    is_prime = [True] * n
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for j in range(p ** 2, n, p):
                is_prime[j] = False
    return [p for p in range(2,n) if is_prime[p]]


_primes = None


def primes_below(n, filename = "primes.txt"):

    global _primes

    if _primes and _primes[-1] > n:
        return _primes

    try: 
        with open(filename, "r") as f:
            primes = list(map(int, f.readlines()))
            if primes and primes[-1] > n:
                _primes = primes
                return primes
    except IOError:
        print("creating file {}".format(filename))

    with open(filename, "w") as f:
        primes = sieve(n)
        f.write("\n".join(map(str, primes)))
        _primes = primes
        return primes


def is_prime(n, filename = "primes.txt"):
    primes = primes_below(n+1, filename)
    i = bisect_left(primes, n)
    return i != len(primes) and primes[i] == n





