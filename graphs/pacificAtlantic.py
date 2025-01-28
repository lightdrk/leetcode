def pacificAtlantic(heights: list[list]) ->list[list]:
    row = len(heights)
    column = len(heights[0])
    output = []
    atl = [[False] * row for _ in range(column)]
    pac = [[False] * row for _ in range(column)]
    def dfs(i,j,reach):
        stack = [(i,j)]
        while stack:
            x,y = stack.pop()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                x+=i
                y+=j
                if 0 <= x <= row-1 and 0 <= y <= column-1 and not reach[x][y]:
                    reach[x][y] = True
                    stack.append((x,y))
    for i in range(row):
        dfs(i,0,pac)
        dfs(0,column-1,atl)

    for j in range(column):
        dfs(0,j,pac)
        dfs(row-1,j,atl)
    print(atl)
    print(pac)


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        row = len(heights)
        column = len(heights[0])
        atlantic = [[False] * column for _ in range(row)]
        pacific = [[False] * column for _ in range(row)]
        def dfs(i,j, reach):
            stack = [(i,j)]
            while stack:
                x,y = stack.pop()
                curr = heights[x][y]
                if 0 < x  and curr <= heights[x-1][y] and not reach[x-1][y]:
                    reach[x-1][y] = True
                    stack.append((x-1,y))
                if x+1 < row and curr <= heights[x+1][y]and not reach[x+1][y]:
                    stack.append((x+1,y))
                    reach[x+1][y] = True
                if 0 < y  and curr <= heights[x][y-1]and not reach[x][y-1]:
                    reach[x][y-1] = True
                    stack.append((x,y-1))
                if y+1 < column  and curr <= heights[x][y+1]and not reach[x][y+1]:
                    stack.append((x,y+1))
                    reach[x][y+1] = True
        output = []

        for i in range(row):
            dfs(i,0,pacific)
            dfs(i,column-1,atlantic)
        for j in range(column):
            dfs(0,j,pacific)
            dfs(row-1,j,atlantic)
        print(pacific)
        print(atlantic)
        for i in range(row):
            for j in range(column):
                if pacific[i][j] and atlantic[i][j]:
                    output.append([i,j])

        return output
pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
a = Solution()
a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])

