def maxProfit(prices: list[int]) -> int:
    obj = {}
    i, index = 0,1
    while i < len(prices):
        obj[prices[index] - prices[i]] = (i, index)
        print(obj)
        index = index + 1
        if index >= len(prices):
            i = i + 1
            index = i
    return obj[max(obj.keys())]

print(maxProfit([7,1,5,3,6,4]))
