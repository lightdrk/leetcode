'''
    first try not good
def maxProfit(prices):
    length = len(prices)
    def recur(i,j):
        if i >= length or j >= length:
            return 0
        money = 0
        if prices[j] > prices[i]:
            money = prices[j]-prices[i] + recur(j+2,j+2)

        return max(money, recur(i+1,j+1), recur(i,j+1))


    return recur(0,0)


print(maxprofit([1,2,3,0,2]))
print(maxprofit([1]))
print(maxprofit([2,1,4]))

'''

def maxProfit(prices):
    length = len(prices)
    def recur(i,hold):
        if i >= length:
            return 0
        
        if hold:
            sell = prices[i] + recur(i+2,0)
            hold = recur(i+1,1)
            return max(sell,hold)
        else:
            buy = recur(i+1,1) - prices[i]
            skip = recur(i+1,0)

            return max(buy,skip)
    return recur(0,0)


print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([2,1,4]))


