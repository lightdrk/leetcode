def climb(n, memo = {}):
    #top down approach
    if memo.get(n):
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2

    memo[n] = climb(n-1, memo) + climb(n-2, memo)
    return memo[n]

print(climb(25))

def climb(n):
    #bottom up approach mean iteration
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo = [0] * (n+1) #[0,0,0,0... n index] for memoriztion
    memo[1] = 1
    memo[2] = 2
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

print(climb(30))

