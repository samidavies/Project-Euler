arr = []    
for i in range(1,1000001):
    count = 1 
    while i  >  1:
        if i % 2 == 0:
            i = i/2
        else:
            i = 3*i+1
        count += 1
    arr.append(count)

print(arr.index(max(arr))+1)


