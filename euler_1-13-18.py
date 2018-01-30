def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


def euler_sum(n):
    if n == 1:
        return 0
    if n == 0:
        return 1
    total = 0
    for k in range(1,n+1):
        if isPrime(k):
            total += k * euler_sum(n-k)
            for j in range(k+1, n-k+1):
                if isPrime(j):
                    total -= j*k*euler_sum(n-k-j)
                    for i in range(j+1, n-k-j+1):
                        if isPrime (i):
                            total += j*k*i*euler_sum(n-k-j-i)
                            for l in range(i+1, n-k-j-i+1):
                                print("here")
                                if isPrime (l):
                                    total -= j*k*i*l*euler_sum(n-k-j-i-l)
                    
    return total


print(euler_sum(16))
print(euler_sum(17))
print(euler_sum(18))
