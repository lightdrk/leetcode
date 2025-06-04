'''
number of islands


'''

def num(grid):
    row = len(grid)
    col = len(grid[0])

    count = 0
    for a in range(row):
        for b in range(col):

            if grid[a][b] == '1':
                print(a,b, grid[a][b])
                count+=1
                grid[a][b] = '-1'
                stack = [(a,b)]
                while stack:
                    i,j = stack.pop()
                    #print(i,j)
                    if -1 < i-1 and 0 < j <col and grid[i-1][j] == '1':
                        grid[i-1][j] = '-1'
                        stack.append((i-1,j))

                    if  -1 < i+1 < row and 0<j<col and grid[i+1][j] == '1':
                        grid[i+1][j] = '-1'
                        stack.append((i+1,j))

                    if -1 < i < row and -1 <j-1<col and grid[i][j-1] == '1':
                        grid[i][j-1] = '-1'
                        stack.append((i,j-1))

                    if -1 < i < row and j+1<col and grid[i][j+1] == '1':
                        grid[i][j+1] = '-1'
                        stack.append((i,j+1))

    print(grid)
    return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(num(grid))
