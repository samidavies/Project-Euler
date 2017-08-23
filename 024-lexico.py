import itertools
#fori i in range(0,3):
#    for j in range(0,3):
#        if j != i:
#            for k in range(0,3):
#                s = ''
#                if k != i and k != j:
#                    s +=str(i)
#                    s += str(j)
#                    s += str(k)
#                    print(s)

count = 0
for p in itertools.permutations(range(10)):
    if count == 999999:
        print(p)
        break
    count += 1




