'''

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


'''
'''
approach is easy here :, what i need to do i iterate over grid and when i hit 1 from their on i do 
DFS, as doing dfs increment the area value till their is nothing to dfs towards.

time complexity will be m*n

'''

def mxArea(grid):
    row, col = len(grid), len(grid[0])
    maximum = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                out = 0
                grid[i][j] = 0
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    out+=1

                    if 0 <= x-1 and grid[x-1][y] == 1:
                        grid[x-1][y] = 0
                        stack.append((x-1,y))

                    if x+1 < row and grid[x+1][y] == 1:
                        grid[x+1][y] = 0
                        stack.append((x+1,y))

                    if 0<= y-1 and grid[x][y-1] == 1:
                        grid[x][y-1] = 0
                        stack.append((x,y-1))

                    if y+1 < col and grid[x][y+1] == 1:
                        grid[x][y+1] = 0
                        stack.append((x,y+1))


                if maximum < out:
                    maximum = out

    return maximum


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(mxArea(grid))
