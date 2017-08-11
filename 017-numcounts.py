# one through nineteen
below_20 = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# one through nine
below_10 = [3, 3, 5, 4, 4, 3, 5, 5, 4]
# twenty through ninety by tens
tens = [6, 6, 5, 5, 5, 7, 6, 6]

count = 0
for i in below_10:
    count += 7
    count += i
    for j in below_20:
        count += i
        count += 10
        count += j
    for k in tens:
        count += i
        count += 10
        count += k
        for m in below_10:
            count += i
            count += 10
            count += k
            count += m
for a in below_20:
    count += a
for m in tens:
    count += m
    for n in below_10:
        count += m
        count += n
count += 11

print(count)


