'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

'''

def ans(grid):
    '''
    interate over every row and do a binary search to get starting of negs
    (m. log n )
    '''
    m,n = len(grid),len(grid[0])
    def binary(row):
        left = 0
        right = n -1
        while left < right:
            mid = left + (right-left)//2
            if grid[row][mid] > -1:
                left = mid+1
            else:
                right = mid
        print(f'start of the negs -> {left} number of negs -> {n-1} - {left}+ 1 => {n-left}')
        return n-left if grid[row][left] < 0 else 0
    total = 0
    for i in range(m):
        total+=binary(i)
    return total

test_case = [[[3,-1,-3,-3,-3],[2,-2,-3,-3,-3],[1,-2,-3,-3,-3],[0,-3,-3,-3,-3]]]#[[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],[[4,3,-1],[3,2,-1],[1,1,-2],[-1,-1,-3]],[[3,2],[1,0]]]

for t in test_case:
    print(ans(t))
