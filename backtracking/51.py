def nQueen(n):
    output = []
    board = ['*'*n for _ in range(n)]
    def backtracking(board, digX, digY, vert, dn):
        if dn == n:
            output.append(board[:])
            return
        for i in range(n):
            if i in vert or (dn-i) in digX or (dn+i) in digY:
                continue
            word = board[dn]
            board[dn] = word[:i] + 'Q' + word[i+1:]
            digX.add(dn-i)
            digY.add(dn+i)
            vert.add(i)
            backtracking(board, digX, digY, vert, dn+1)
            board[dn] = word
            digX.remove(dn-i)
            digY.remove(dn+i)
            vert.remove(i)
    backtracking(board,set(),set(),set(), 0)
    return output

print(nQueen(4))

print(nQueen(1))

print(nQueen(5))
