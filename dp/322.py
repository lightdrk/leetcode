def coinChange(coins: list[int], amount: int) -> int:
    length = len(coins)
    def recur(val, step):
        if val == amount:
            return step
        ans = float('inf')
        for n in coins:
            if val+n > amount:
                continue
            ans = min(ans, recur(val+n,step+1))

        return ans if ans != float('inf') else -1
    return recur(0,0)

print(coinChange([1,2,5], 11))
print(coinChange([1,2,5], 100))

print(coinChange([2], 3))

print(coinChange([2], 4))

print(coinChange([2], 1))
