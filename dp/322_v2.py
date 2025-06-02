#def coin(coins, amount):
#    length = len(coins)
#    def recur(a):
#        if a == 0:
#            return 0
#        if a < 0:
#            return float('inf')
#        min_m = float('inf')
#        for i in range(length):
#            ans = recur(a - coins[i])
#            if ans != float('inf'):
#                min_m = min(ans +1, min_m)
#
#        return min_m
#    ans = recur(amount)
#    return  ans if ans != float('inf') else -1

'''
here this tabulation creation was kinda hard for me 

here we have created dp with amount , to get coins needed to reach 


'''


def coin(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0

    for i in range(amount+1):
        if dp[i] == float('inf'):
            continue
        for coin in coins:
            if coin+i > amount:
                continue
            dp[coin+i] = min(dp[i]+1, dp[coin+i])

    return dp[amount] if dp[amount] != float('inf') else -1


print(coin([1,2,5], 11))
print(coin([2], 3))
