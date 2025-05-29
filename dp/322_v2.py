def coin(coins, amount):
    length = len(coins)
    def recur(a):
        if a == 0:
            return 0
        if a < 0:
            return float('inf')
        min_m = float('inf')
        for i in range(length):
            ans = recur(a - coins[i])
            if ans != float('inf'):
                min_m = min(ans +1, min_m)

        return min_m
    ans = recur(amount)
    return  ans if ans != float('inf') else -1

print(coin([1,2,5], 11))
print(coin([2], 3))

def coin(coins, amount):

