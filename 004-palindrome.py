def palindrome(n):
    s = str(n)
    back = s[::-1]
    return s == back


def findpal():
#    big = 0
#    for a in range(100,1000):
#        for b in range(100,1000):
#            k = a * b
#            if palindrome(k) and k > big:
#                big = k
#    return big

    return max(
        a * b
        for a in range(100,1000)
        for b in range(100,1000)
        if palindrome(a * b)
    )


print(findpal())

