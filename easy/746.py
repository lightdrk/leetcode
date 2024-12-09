def minCost(cost):
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2,len(cost)):
        dp[i] = dp[i-2] + cost[i]
    print(dp)

print(minCost([1,100,1,1,1,100,1,1,100,1]))
