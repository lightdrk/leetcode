#surrounded Regions

def solve(board):
    a = len(board)
    b = len(board[0])
    def dfs(i,j):
        stack = [(i,j)]
        while stack:
            x,y = stack.pop()
            if x+1 < a and board[x+1][y] == '1':
                board[x+1][y] = 'T'
                stack.append((x+1,y))

                if 0 < x and board[x-1][y] == '1':
                    board[x-1][y] = 'T'
                    stack.append((x-1,y))

                    if y+1 < b and board[x][y+1] == '1':
                        board[x][y+1] = 'T'
                        stack.append((x,y+1))

                    if 0 < y and board[x][y-1] == '1':
                        board[x][y-1] = 'T'
                        stack.append((x,y-1))

    for i in range(a):
        for j in [0,b-1]:
            if board[i][j] == 'O':
                board[i][j] = "T"
                dfs(i,j)

    for j in range(1,b-1):
        for i in [0,a-1]:
            if board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i,j)

    for row in range(a):
        for col in range(b):
            if board[row][col] == 'O':
                board[row][col] = 'X'

            if board[row][col] == 'T':
                board[row][col] = 'O'
    print(board)


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(board)
solve(board)
