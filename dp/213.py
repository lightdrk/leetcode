def rob(nums):
    length = len(nums)
    cache = {}
    def recur(idx):
        if length&1 == 1:
            if idx >= length-1:
                return 0
        else:
            if idx >= length:
                return 0
        if idx in cache:
            return cache[idx]
        cache[idx] = nums[idx] + recur(idx+2)
        cache[idx+1] = recur(idx+1)

        return max(cache[idx],cache[idx+1])
    return recur(0)


print(rob([2,3,2]))


