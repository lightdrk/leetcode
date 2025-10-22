'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

'''

def minimizes(grid):
    m,n = len(grid), len(grid[0])

    def dp(i,j):
        if i > (m -1) or j > (n-1):
            return float('inf')
        if i == m-1 and j == n-1:
            return grid[i][j]
        
        return min(dp(i+1,j),dp(i,j+1)) + grid[i][j]

    return dp(0,0)


def minimizes(grid):
    m,n = len(grid), len(grid[0])

    def dp(i,j):
        if i > (m -1) or j > (n-1):
            return float('inf')
        if i == m-1 and j == n-1:
            return grid[i][j]
        
        return min(dp(i+1,j),dp(i,j+1)) + grid[i][j]

    return dp(0,0)


edge = [[[1,3,1],[1,5,1],[4,2,1]]]
for case in edge:
    print(minimizes(case))
