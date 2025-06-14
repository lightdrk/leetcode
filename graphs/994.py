from collections import deque

def rotting(grid):
    row = len(grid)
    col = len(grid[0])
    def bfs(i,j):
        que = deque([(i,j,0)])
        ans = 0
        while que:
            x,y,z = que.popleft()
            if z > ans:
                ans = z

            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                i+=x
                j+=y
                if 0 <= i and i < row and 0 <= j and j < col and grid[i][j] == 1:
                    grid[i][j] = 2
                    que.append((i,j,z+1))
        return ans

    
    mx = -1
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 2:
                mx = max(mx,bfs(r,c))

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                return -1

    return mx

'''
not proper answer 

'''
print(rotting([[2,1,1],[1,1,0],[0,1,1]]))

print(rotting([[0,2]]))
print(rotting([[2,1,1],[0,1,1],[1,0,1]]))
