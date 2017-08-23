f = open('p022_names.txt')
full = f.read()
arr = full.split(",")
srtd = sorted(arr)
scores = []
for i in srtd:
    score = 0
    current = list(i)
    for j in current:
        if ord(j) != 34:
            score += ord(j)-64
    ind = srtd.index(i)+1
    scores.append(score * ind )

print(sum(a for a in scores))
