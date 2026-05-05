'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

'''
test_case = [1,2,3,4,5]


def totalQueens(n)-> int:
    visited = [(0,0)]
    count = [0]
    def bk(i,j,x):
        if x==n:
            count[0]+=1
            return
        if i < 0 or i >= n:
            return 
        if j < 0 or j >= n:
            return

        
        for ii,jj in visited:
            if ii == i or jj == j or (jj-ii) == (j-i):
        visited.append((i+1,j))
        bk(i+1,j,x+1)
        visited.pop()

        visited.append((i,j+1))
        bk(i,j+1,x+1)
        visited.pop()

        visited.append((i-1,j))
        bk(i-1,j,x+1)
        visited.pop()

        visited.append((i,j-1))
        bk(i,j-1,x+1)
        visited.pop()


    bk(0,0,1)
    return count[0]


for t in test_case:
    print(totalQueens(t))










































