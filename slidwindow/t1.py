import heapq

def slidingWindowMaximum(nums:list, k:int):
    l = len(nums)
    if k > l:
        return [max(nums)]
    heap = []
    output = []
    for i in range(k):
        heapq.heappush(heap,(-nums[i],i))
    output.append(-heap[0][0])
    for i in range(k,l):
        heapq.heappush(heap,(-nums[i],i))
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        output.append(-heap[0][0])

    return output

edge = [(1,[1,2,2]), (2,[4,2,1,4,4])]
for k,l in edge:
    print(slidingWindowMaximum(l,k))
