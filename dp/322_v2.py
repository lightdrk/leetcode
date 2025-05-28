def coin(coins, amount):
    length = len(coins)
    ans = [0]
    def recur(i,a):
        if a == 0:
            return True
        if i >= length:
            return False
        if a >= coins[i]:
            what = (recur(i+1, a-coins[i]) or recur(i+1, a))
        return ans

    return recur(0,amount)

print(coin([1,2,5], 11))
print(coin([2], 3))
