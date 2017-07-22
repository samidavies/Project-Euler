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


