def exists(board,word):
    length = len(word)
    row = len(board)
    column = len(board[0])
    output = [False]
    def bk(x,y,idx,s,visited):
        if not board[x][y] == word[idx]:
            return
        print(s)
        if idx == length-1 and s == word:
            output[0] = True
            return
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0 <= x+i < row and 0 <= y+j < column and not (x+i,y+j) in visited:
                bk(x+i, y+j, idx+1, s+board[x+i][y+j], visited)
    for i in range(row):
        for j in range(column):
            if board[i][j] == word[0]:
                bk(i,j,0,board[i][j], {(i,j)})
    return output[0]

print(exists([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))

print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))

print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'))

print(exists([["A","A"]], 'AAA'))

print(exists([["a","b"],["c","d"]], 'cdba'))


