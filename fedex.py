 

c = 0.9
print(c)
for i in range(1,300000):
    new = 4*c/(4*c + (c-2) ** 2)
    c = new
    print c

    







