def exist(board,word):
    row,col = len(board), len(board[0])
    l = len(word)
    def walk(r,c,i):
        if i == l:
            return True 
        if 0 > r or r >= row or 0 > c or c >= col or board[r][c] != word[i]:
            return False
        i+=1
        ans = False
        tmp = board[r][c] 
        board[r][c] = ''
        ans|=walk(r+1,c,i)
        ans|=walk(r-1,c,i)
        ans|=walk(r,c+1,i)
        ans|=walk(r,c-1,i)
        board[r][c] = tmp
        return ans
    for r in range(row):
        for c in range(col):
            if board[r][c] == word[0]:
                if walk(r,c,0):
                    return True
    return False

test_case = [[[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"], [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"], [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"DDGG"]]
for board,word in test_case:
    print(exist(board,word))
