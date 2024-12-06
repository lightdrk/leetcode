# working with matrix binary search

'''
[
[1,3,4,5],
[7,9,10,22],
[23,24,27,29]
]
target = 24


matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
target = 5

'''

#Time Complexity: --O( m * n) 
#bad appraoach as this approach is m*n not log 
#beacuse row is traversed one by one 
'''
        if not matrix and not matrix[0]:
            return False
        left = 0
        m_l = len(matrix) - 1
        length = len(matrix[0]) - 1
        right = length
        row = 0
        while left <= right:
            mid = left + (right - left) // 2
            ans = matrix[row][mid]
            if ans == target:
                return True
            if ans > target:
                right = mid - 1
            else:
                left = mid + 1
                if left > length:
                    row = row + 1
                    if row > m_l:
                        return False
                    left = 0

        return False
'''

def searchMatrix(matrix: list[list[int]], target: int) ->bool:
    #log (n) + log (m) == log(n*m)
    #we can search for which row can possible have target
    #we can bin search the rows only
    intial = 0
    row = len(matrix) - 1
    #this will find the row on which their is possibility of finding target
    while intial <= row:
        mid = intial + (row - intial)//2

        ans = matrix[mid][0]
        if ans == target:
            return True
        if ans > target:
            row = mid - 1
        else:
            intial = mid + 1
    print(row)
    if row < 0 or row >= len(matrix):
        return False
    left = 0
    right = len(matrix[0]) - 1
    while left <= right :
        mid = left + (right - left)//2
        ans = matrix[row][mid]
        if ans == target:
            return True
        if ans > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(searchMatrix([[1,3,4,5],[7,9,10,22],[23,24,27,29]], 29))
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
target = 5
print(searchMatrix(matrix, target))
