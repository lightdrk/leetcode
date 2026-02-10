'''
1. matrix of words 
2. can not be used more than once in a run 
'''

def exists(board,word):
    row, col = len(board), len(board[0])
    l = len(word)
    def branch(i,j,c,visited):
        if c >= l:
            return True
        if board[i][j] != word[c] or (i,j) in visited:
            return False
        c+=1
        ans = False
        v = visited.copy()
        v.add((i,j))
        if i < row:
            ans |= branch(i+1,j,c,v)
        if j < col :
            ans |= branch(i,j+1,c,v)
        return ans
    return branch(0,0,0,set())

