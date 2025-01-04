def isT(grid):
    li = len(grid)
    lj = len(grid[0])
    for i in range(li):
        for j in range(lj):
            if grid[i][j] == 0:
                stack = [(i,j,0)]
                while stack:
                    x,y,distance = stack.pop()
                    distance+=1
                    if x+1 < li and grid[x+1][y] > distance:
                        grid[x+1][y] = distance
                        stack.append((x+1,y,distance))

                    if x > 0 and grid[x-1][y] > distance:
                        grid[x-1][y] = distance
                        stack.append((x-1,y,distance))

                    if y+1 < lj and grid[x][y+1] > distance:
                        grid[x][y+1] = distance
                        stack.append((x,y+1,distance))

                    if y > 0 and grid[x][y-1] > distance:
                        grid[x][y-1] = distance
                        stack.append((x,y-1,distance))
    print(grid)


grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

grid1 = [    [-1, -1, -1, -1, -1],
    [-1, 222222222222222, 222222222222222, -1, -1],
    [-1, 222222222222222, 0, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1]
]
grid2 = [    [-1, -1, -1, -1, -1],
    [-1, 222222222222222, 222222222222222, -1, -1],
    [-1, 222222222222222, 0, -1, -1],
    [-1, -1, -1, 222222222222222, -1],
    [-1, -1, -1, -1, -1]
]

grid3 = [    [-1, -1, -1, -1, -1],
    [-1, 222222222222222, -1, -1, -1],
    [-1, 222222222222222, 0, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1]
]

isT(grid)
isT(grid1)
isT(grid2)
isT(grid3)
