import math
def eating(piles,hour):
    low = 1
    high = max(piles)
    def yes(rate):
        sm = sum(math.ceil(p/rate) for p in piles)
        return sm <= hour
    ans = 0
    while low <= high:
        mid = (low+high)//2
        if yes(mid):
            ans = mid
            high= mid-1
        else:
            low = mid+1

    return ans 


print(eating([3,6,7,11],8))
