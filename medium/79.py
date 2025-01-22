def exists(board,word):
    length = len(word)
    row = len(board)
    column = len(board[0])
    output = [False]
    def bk(x,y,idx,s):
        if not board[x][y] == word[idx]:
            return
        if idx == length-1 and s == word:
            output[0] = True
            return
        tmp,board[x][y] = board[x][y], '#'
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0 <= x+i < row and 0 <= y+j < column:
                bk(x+i, y+j, idx+1, s+board[x+i][y+j])
        board[x][y] = tmp

    for i in range(row):
        for j in range(column):
            if board[i][j] == word[0]:
                bk(i,j,0,board[i][j])
    return output[0]

def exists_dfs(board,word):
    length = len(word)
    row = len(board)
    column = len(board[0])
    def dfs(st):
        while st:
            i,j,idx = st.pop()
            if idx == length-1:
                return True
            tmp,board[i][j] = board[i][j],'#'
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                x+=i
                y+=j
                if 0 <= x < row and 0 <= y < column and board[x][y] == word[idx+1]:
                    st.append((x,y,idx+1))
            board[i][j] = tmp
        return False
    for i in range(row):
        for j in range(column):
            if board[i][j] == word[0]:
                print(i,j)
                if dfs([(i,j,0)]):
                    return True
    return False


print(exists([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))

print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))

print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'))

print(exists([["A","A"]], 'AAA'))

print(exists([["a","b"],["c","d"]], 'cdba'))

print(exists([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))



print('*************dfs**************')




print(exists_dfs([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
#
print(exists_dfs([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
#
print(exists_dfs([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))

print(exists_dfs([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'))

print(exists_dfs([["A","A"]], 'AAA'))

print(exists_dfs([["a","b"],["c","d"]], 'cdba'))

print(exists_dfs([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))



