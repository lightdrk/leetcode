import heapq
from collections import Counter

def findXSum(nums, k, x):
    hash_map = Counter(nums[:k])
    output = []
    for i in range(len(nums) - k + 1):
        if i>0:
            hash_map[nums[i-1]]-=1
            if hash_map[nums[i-1]] == 0:
                del hash_map[nums[i-1]]
            if not nums[i+k-1] in hash_map:
                hash_map[nums[i+k-1]] = 0
            hash_map[nums[i+k-1]]+=1
        que = []
        for val, freq in hash_map.items():
            heapq.heappush(que,(-freq, -val))
        sm = 0
        print('top', que)
        for _ in range(x):
            if que:
                val, freq = heapq.heappop(que)
                sm+=val*freq
        output.append(sm)
    return output

print(findXSum([1,1,2,2,3,4,2,3],6,2))

