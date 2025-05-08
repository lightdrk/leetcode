def coinChange(coins: list[int], amount: int) -> int:
    length = len(coins)
    memo = {}
    def recur(val):
        if val == amount:
            return 0
        if val in memo:
            return memo[val]
        ans = float('inf')

        for n in coins:
            if val+n > amount:
                continue
            ans = min(ans, 1+recur(val+n))
        memo[val] = ans
        return ans
    
    output = recur(0)
    print(memo)
    return output if output != float('inf') else -1

print(coinChange([1,2,5], 11))
print(coinChange([1,2,5], 100))

print(coinChange([2], 3))

print(coinChange([2], 4))

print(coinChange([2], 1))
