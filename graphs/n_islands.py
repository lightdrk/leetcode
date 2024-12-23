def n_island(grid):
    a = len(grid)
    b = len(grid[0])
    island = 0
    for i in range(a):
        for j in range(b):
            if grid[i][j] == '1':
                island+=1
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if x+1 < a and grid[x+1][y] == '1':
                        grid[x+1][y] = '0'
                        stack.append((x+1,y))

                    if 0 < x and grid[x-1][y] == '1':
                        grid[x-1][y] = '0'
                        stack.append((x-1,y))

                    if y+1 < b and grid[x][y+1] == '1':
                        grid[x][y+1] = '0'
                        stack.append((x,y+1))

                    if 0 < y and grid[x][y-1] == '1':
                        grid[x][y-1] = '0'
                        stack.append((x,y-1))

    return island

grid =[["1","1","1"],["0","1","0"],["1","1","1"]]
print(n_island(grid))
