test_case = [[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],[[1]],[[1,1],[1,1]]]


def perimeter(matrix):
    row,col = len(matrix),len(matrix[0])
    stack = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                stack.append((i,j))
                break
        if stack:
            break

    perimeter = 0
    while stack:
        print(stack, matrix, perimeter)
        i,j = stack.pop()
        if matrix[i][j] == 2:
            continue
        matrix[i][j] = 2
        if i+1 >= row or matrix[i+1][j] == 0:
            perimeter+=1
        elif matrix[i+1][j] == 1:
            stack.append((i+1,j))
        if j+1 >= col or matrix[i][j+1] == 0:
            perimeter+=1
        elif matrix[i][j+1] == 1:
            stack.append((i,j+1))

        if i-1<0 or matrix[i-1][j] == 0:
            perimeter+=1
        elif matrix[i-1][j] == 1:
            stack.append((i-1,j))
        if j-1<0 or matrix[i][j-1] == 0:
            perimeter+=1
        elif matrix[i][j-1] == 1:
            stack.append((i,j-1))

    return perimeter


for t in test_case:
    print(perimeter(t))
