def spiral(matrix):
    i = 0
    j = 0
    li = len(matrix)
    lj = len(matrix[0])
    output = []
    while i < li and j < lj:
        for b in range(j,lj):
            output.append(matrix[i][b])
        i+=1
        for a in range(i,li):
            output.append(matrix[a][lj-1])
        lj-=1
        if i < li:
            for b in range(lj-1,j-1,-1):
                output.append(matrix[li-1][b])
            li-=1
        if j < lj:
            for a in range(li-1,i-1,-1):
                output.append(matrix[a][j])
            j+=1
    print(output)

matrix = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24]]
spiral(matrix)
print(matrix)
