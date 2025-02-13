def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    row = len(board)
    column = len(board[0])
    def isPossible(word):
        outbound = len(word)
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0]:
                    stack = [(i,j,0,set())]
                    while stack:
                        print(stack)
                        x,y,idx,visited = stack.pop()
                        for ii,jj in [(1,0),(-1,0),(0,1),(0,-1)]:
                            ii+=x
                            jj+=y
                            if idx+1 >= outbound:
                                return True
                            if row > ii >= 0 and column > jj >= 0 and board[ii][jj] == word[idx+1] and not (ii,jj) in visited:
                                visited.add((x,y))
                                stack.append((ii,jj,idx+1,visited))
        return False
    output = []
    for word in words:
        print()
        if isPossible(word):
            output.append(word)
    return output
board = [["a","b","e"],["b","c","d"]]
words = ["abcdeb"]
print(findWords(board,words))

