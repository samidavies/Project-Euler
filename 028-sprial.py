from itertools import cycle, tee, izip 

def make_grid(n):

    grid = [[0 for i in range(n)] for j in range(n)]


    count = iter(range(1, n ** 2 + 1))
    grid[n/2][n/2] = next(count)
    grid[n/2][n/2 + 1] = next(count)

    c = cycle([(0,1), (1,0), (0,-1), (-1,0)])  

    dir0, dir1 = tee(c)
    next(dir1)


    i = n/2 
    j = n/2 + 1
    for (i0, j0), (i1, j1) in izip(dir0, dir1):
        while True:
            if grid[i + i1][j+j1] == 0:
                break 
            i += i0
            j += j0
            try:
                grid[i][j] = next(count)
            except StopIteration:
                return grid

n = 1001

grid = make_grid(n)

total = -1
for i in range(n):
    total += grid[i][i] + grid[i][n-1-i]

print(total)




