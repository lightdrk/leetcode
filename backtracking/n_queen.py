def queen(n :int):
    output = []
    board = [['.'] * n for _ in range(n)]
    used = set()
    def bk(queen,ld,rd,si,sj):
        if queen == n:
            out_a = tuple(''.join(board[i]) for i in range(n))
            if out_a in used:
                return
            used.add(out_a)
            output.append(list(out_a))
            return
        for i in range(n):
            if i in si:
                continue
            for j in range(n):
                if j in sj:
                    continue
                if (i-j) in ld or (i+j) in rd:
                    continue
                if board[i][j] == '.':
                    board[i][j] = 'q'
                    ld.add(i-j)
                    rd.add(i+j)
                    si.add(i)
                    sj.add(j)
                    bk(queen+1,ld,rd,si,sj)
                    ld.remove(i-j)
                    rd.remove(i+j)
                    si.remove(i)
                    sj.remove(j)
                    board[i][j] = '.'

    bk(0,set(),set(),set(),set())
    return output
print(queen(8))
