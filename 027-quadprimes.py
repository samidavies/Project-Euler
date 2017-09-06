from itertools import count
from multiprocessing import Pool

import helper_functions as hf


def count_conprimes(a,b):
    if b == 0:
        print(a,b)
    for k in count():
        test = k * k + a * k + b
        if not hf.is_prime(test):
            return k

def get_arg((a,b)):
    return count_conprimes(a,b), (a,b)


x = ((a, b) for a in range(-999,1000) for b in range(-999, 1000))
p = Pool()
l = p.map(get_arg, x)
con, (a,b) = max(l)
print((a,b), a * b, con)




    
