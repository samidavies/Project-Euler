tri = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 06, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33 ],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

def long(n):
    new_arr = []
    if n == 0:
        return tri[0]
    arr = long(n-1)
    l = len(tri[n])
    for i in range(l):
        if 0 < i < l-1:
            m = max(arr[i-1]+tri[n][i], arr[i]+tri[n][i])
        if i == 0:
            m = arr[i]+tri[n][i]
        if i == l-1:
            m = arr[i-1]+tri[n][i]
        new_arr.append(m)
    return new_arr

print(max(long(len(tri)-1)))

def solution(i):
    row = tri[i]
    if i == 0:
        return row
    prev = solution(i-1)
    return [
        r + max(a,b)
        for r, a, b in zip(row, [0]+prev, prev+[0])
    ]


