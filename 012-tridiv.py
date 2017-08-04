import math

def count_divisors(n): 
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1

    return count

# def fast_count_divisors(n):
#    arr = []
#    div = [1,n]
#    if n % 2 == 0:
#        arr.append(2)
#         while n % 2 == 0:
#            n = n /2
#    for i in range(3,int(math.sqrt(n)) + 1 , 2):
#        if n % i == 0:
#            arr.append(i)
#            while n % i == 0:
#                count += 1
#                n = n/i
#    if n>2:
#        arr.append(n)
#    if len(arr) < 2:
#        return 2 



    


            

def tri(m):
    return sum( i for i in range(1,m+1))

def tri_count_div(k):
    return count_divisors(tri(k))


def find_tri(j):
    current = 1
    while tri_count_div(current) < j:
        current += 1

    return tri(current)




