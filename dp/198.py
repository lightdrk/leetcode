def rob(nums):
    length = len(nums)
    cache = {}
    def rc(idx):
        if length <= idx:
            return 0
        if idx in cache:
            return cache[idx]
        cache[idx] = nums[idx] + rc(idx+2)
        cache[idx+1] = rc(idx+1)
        return max(cache[idx],cache[idx+1])
    return rc(0) 

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([1,3,1,3,100]))

