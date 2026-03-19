def solveNQueens(n):
    solution = []
    sol = ['.'*n]*n
    def bk(dn,x,y,position,sol):
        if dn == 0:
            solution.append(sol[:])
            return
        for i in range(n):
            for j in range(n):
                if (i,j) in position:

        bk(dn-1,x,y,position,sol)

