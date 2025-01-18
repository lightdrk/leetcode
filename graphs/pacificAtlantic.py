def pacificAtlantic(heights: list[list]) ->list[list]:
    row = len(heights)
    column = len(heights[0])
    pacific = set()
    atlantic = set()
    output = set()
    visited = set()
    def dfs(node):
        stack = [node]
        pt = 0
        at = 0
        while stack:
            i,j = stack.pop()
            prev = heights[i][j]
            if pt and at:
                output.add((node))
                return
            if (i,j) in pacific:
                pt=1
            if (i,j) in atlantic:
                at=1
            if not (i,j) in visited:
                visited.add((i,j))
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                x+=i
                y+=j
                if 0<x<row and 0<y<column and heights[x][y] > prev:
                    stack.append((x,y))
    for i in range(row):
        pacific.add((i,0))
        atlantic.add((i,column-1))
    for j in range(column):
        pacific.add((0,j))
        atlantic.add((row-1,j))
    for i in range(row):
        for j in range(column):
            dfs((i,j))
    return output

print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
