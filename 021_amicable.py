import math
from helper_functions import divisors 

amicables = set()
for i in range(1,10000):
    di = sum(k for k in divisors(i))-i
    ddi = sum( j for j in divisors(di))-di
    if ddi == i and di != ddi:
        amicables.add(i)
        amicables.add(di)
print(amicables)
print(sum(a for a in amicables))

