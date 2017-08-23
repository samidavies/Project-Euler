def fib(n):
    if n == 1 or n== 2:
        return 1
    return fib(n-1) + fib(n-2)


def fibfast():
    p1 = 1
    p2 = 1
    yield p1
    yield p2
    while True:
        p1, p2 = p2, p1 + p2
        yield p2
        
#note off by 1
for i,f in enumerate(fibfast()):
    s = str(f)
    if len(s) >= 1000:
        print(i)
        print(s)
        break

        

