'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

'''
test_case = [1,2,3,4,5]

'''
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
        visited.pop()t


    bk(0,0,1)
    return count[0]
'''

'''
def totalAdmins(t):
    counter = [0]
    def bk(count,ix,jy,i,j):
        if count == t:
            counter[0]+=1
            return
        for x in range(t):
            if x in i:
                continue
            for y in range(t):
                if (y in j) or ( (x-y) in ix) or ((x+y) in jy) :
                    continue
                ix.add((x-y))
                jy.add(x+y)
                i.add(x)
                j.add(y)
                bk(count+1,ix,jy,i,j)
                ix.remove((x-y))
                jy.remove(x+y)
                i.remove(x)
                j.remove(y)
    bk(0,set(),set(),set(),set())

    return counter[0]

Above did not work beacuse we are not looking for duplicate position because queen can be placed in different order 
same position but in different order 

'''

def totalAdmins(t):
    counter = [0]
    def bk(row,dx,dy,cols):
        if row == t:
            counter[0]+=1
            return
        for i in range(t):
            if i in cols or ((row-i) in dx) or ((row+i) in dy):
                continue
            dx.add(row-i)
            dy.add(row+i)
            cols.add(i)
            bk(row+1,dx,dy,cols)
            dx.remove(row-i)
            dy.remove(row+i)
            cols.remove(i)
    bk(0,set(),set(),set())
    return counter[0]

for t in test_case:
    print(totalAdmins(t))

































