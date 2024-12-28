''' this file is to  test out error '''

def solve(board: list[list[str]]) -> None:
    li = len(board)
    print(li)
    lj = len(board[0])
    print(lj)
    def dfs(i,j):
        stack = [(i,j)]
        while stack:
            i,j = stack.pop()
            if i+1 < li and board[i+1][j] == 'O':
                board[i+1][j] = 'T'
                stack.append((1+i,j))

                if i-1 > 0 and board[i-1][j] == 'O':
                    board[i-1][j] = 'T'
                    stack.append((i-1,j))

                if j+1 < lj and board[i][j+1] == 'O':
                    board[i][j+1] = 'T'
                    stack.append((i,j+1))

                if j-1 > 0 and board[i][j-1] == 'O':
                    board[i][j-1] = 'T'
                    stack.append((i,j-1))


    for i in range(li):
        for j in [0,lj-1]:
            if board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i,j)

    for j in range(lj):
        for i in [0,li-1]:
            if board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i,j)

    for i in range(li):
        for j in range(lj):
            if board[i][j] == 'O':
                board[i][j] = 'X'

            if board[i][j] == 'T':
                board[i][j] = 'O'


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)
print(board)
