import math


def get_digits(d):
    r = 1
    arr =[1]
    for j in range(1,2*d-1):
        n, r = divmod(r * 10, d)
        if r in arr:
            break
        arr.append(r)
    return arr


        
print( max(
    (d for d in range(1,1000)),
    key = lambda d: len(get_digits(d))
))
