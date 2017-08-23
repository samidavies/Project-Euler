from  helper_functions import divisors

def abund_list(m):
    abund = []
    for i in range(2,m):
        divs = list(divisors(i))
        proper = [d for d in divs if d != i ]
        s = sum(a for a in proper)
        if s > i:
            abund.append(i)
    abund.sort()
    return abund
    
def sumable(max_sum,abund):
    return {
        a + b 
        for a in abund 
        for b in abund 
        if a+b <= max_sum
    }


total = 0
keep = abund_list(28125)
sumables = sumable(28125, keep)
not_sumable = [a for a in range(1,28125) if a not in sumables]
print(not_sumable)
print(sum(not_sumable))


