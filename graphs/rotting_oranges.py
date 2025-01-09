from collections import deque

def rotten(grid):
    visited = set()
    def multi_origin_bfs(starting):
        time = 0
        queue = deque(starting)
        while queue:
            lvl = len(queue)
            while lvl:
                x,y = queue.popleft()
                if not (x,y) in visited:
                    visited.add((x,y))
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    queue.append((x-1,y))
                if x+1 < row and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    queue.append((x+1,y))

                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    queue.append((x,y-1))
                if y+1 <column and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    queue.append((x,y+1))
                lvl-=1
            time+=1
        return time-1
    row = len(grid)
    column = len(grid[0])
    rotten_set = set()
    fresh_set = set()
    for i in range(row):
        for j in range(column):
            val = grid[i][j]
            if val == 2:
                rotten_set.add((i,j))

            if val == 1:
                fresh_set.add((i,j))
    if not fresh_set:
        return 0
    time = multi_origin_bfs(rotten_set)
    if not visited == (rotten_set|fresh_set):
        return -1
    return time


print(rotten([[2,1,1],[1,1,0],[0,1,1]]))
print(rotten([[2,1,1],[0,1,1],[1,0,1]]))

print(rotten([[0,2]]))

print(rotten([[0]]))
