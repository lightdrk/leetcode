def uniquePaths(n,m):
    memo = {}
    def recur(x,y):
        if x == n-1 and y == m-1:
            return 1
        if (x,y) in memo:
            return memo[(x,y)]
        if x >= n:
            return 0
        if y >= m:
            return 0
        memo[(x,y)] = recur(x+1,y)+recur(x,y+1)
        return memo[(x,y)]
    return recur(0,0)

print(uniquePaths(3,7))
print(uniquePaths(3,2))
print(uniquePaths(100,100))

