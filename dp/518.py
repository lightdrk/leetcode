def coinChange(amount, coins):
    length = len(coins)
    memo = {}
    def recur(sum,idx):
        if sum == amount:
            return 1
        if sum > amount:
            return 0
        if idx >=length:
            return 0
        if (sum,idx) in memo:
            return memo[(sum,idx)]

        include = recur(sum+coins[idx], idx)
        exclude = recur(sum, idx+1)
        memo[(sum,idx)] = include+exclude;
        return memo[(sum,idx)]
    return recur(0,0)


print(coinChange(5,[1,2,5]))
print(coinChange(10,[10]))
print(coinChange(500, [1,2,5]))



