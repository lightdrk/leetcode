def solveNQueens(n):
    output = []
    matrix = ['.'*(n)]*n
    def bk(i,dx,dy,v):
        if i >= n:
            output.append(matrix[:])
            return
        for j in range(n):
            if (j in v) or (i-j in dx) or (i+j in dy):
                continue
            old = matrix[i]
            matrix[i] = matrix[i][:j]+'Q'+matrix[i][j+1:]
            dx.add(i-j)
            v.add(j)
            dy.add(j+i)
            bk(i+1,dx,dy,v)
            dx.remove(i-j)
            dy.remove(i+j)
            v.remove(j)
            matrix[i] = old

    bk(0,set(),set(),set())
    return output

for t in range(1,7):
    print(solveNQueens(t))


