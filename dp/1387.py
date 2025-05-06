import heapq

def getKth(lo: int, hi: int, k: int) -> int:
    cache = {}
    def recursion(val):
        if val in cache:
            return cache[val]
        if val == 1:
            return 0
        if val&1 == 1:
            steps = 1+recursion((val*3)+1)
        else:
            steps = 1+recursion((val//2))

        cache[val] = steps
        return steps
    pq = []
    count = 0
    for i in range(lo,hi+1):
        steps = recursion(i)

        heapq.heappush(pq, (-steps, i))
        count+=1
        if count >= k:
            heapq.heappop(pq)
    result = sorted(pq, key=lambda x: (-x[0], x[1]))
    print(result)
    return result.pop()[1]


getKth(1,1000,777)
