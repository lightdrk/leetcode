''' set matrix to zero '''

def setZeros(matrix: list[list[int]]) -> None:
    print(matrix)
    m = set()
    for i in range(len(matrix)):
        if 0 in matrix[i]:
            for z,n in enumerate(matrix[i]):
                if 0 == n:
                    m.add(z)
            matrix[i][:] = [0] * len(matrix[i])
    print(m)
    for i in range(len(matrix)):
        for x in m :
            if x < len(matrix[i]):
                matrix[i][x] = 0



matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeros(matrix)
print(matrix)

