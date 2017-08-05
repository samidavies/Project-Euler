import math

_divisors = {}

def divisors(n):
    result = set()
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            result.add(i)
            result.add(n/i)
    return result



def count_divisors(m):
    tri = m*(m+1)/2
    if m % 2 == 0:
        divs =  divisors(m/2) | divisors(m+1)
    else:
        divs = divisors((m+1)/2) | divisors(m)
    divs |= { j*k for j in divs for k in divs if tri % (j*k) == 0 and j*k <= tri}
    comp = { tri/i for i in divs }
    print(m, sorted(list(comp | divs)) )
    print(m, len(comp | divs) )
    return len(comp | divs)

m=1
while count_divisors(m) < 500:
    m += 1
print(m)




    

            





