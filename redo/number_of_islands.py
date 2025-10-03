'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

def numIslands(grid: list) -> int:
    row = len(grid)
    col = len(grid[0])
    '''
        def dfs(i,j):
            if i < 0 or i >= row:
                return
            if j < 0 or j >= col:
                return
            if grid[i][j] != '1':
                return

            grid[i][j] = -1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        '''
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                stack = [(i,j)]
                while stack:
                    n,m = stack.pop()
                    grid[n][m] = -1
                    for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                        x+=n
                        y+=m
                        if -1 < x < row and -1 < y < col and grid[x][y] == '1':
                            stack.append((x,y))
                count+=1

    return count

def perimiterOfIsland(grid) -> tuple:
    row = len(grid)
    col = len(grid[0])
    count = 0
    totalP = 0
    size = {}
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                stack = [(i,j)]
                sz = 0
                while stack:
                    n,m = stack.pop()
                    sz+=1
                    grid[n][m] = -1
                    for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                        x+=n
                        y+=m
                        if -1 < x < row and -1 < y < col:
                            if grid[x][y] == '1':
                                stack.append((x,y))
                            elif grid[x][y] == '0' or 0 > x or x > row or 0 > y or y > col:
                                totalP+=1
                count+=1
                size[sz] = size.get(sz,0) + 1

    print(size)
    return (count, totalP)

test = [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], [["0","0","0"],["0","1","0"],["0","0","0"]]]

for grid in test:
    print(perimiterOfIsland(grid))

