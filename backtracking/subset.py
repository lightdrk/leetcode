def subSet(nums):
    result = []
    if not nums:
        return result
    def bk(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            bk(i+1, current)
            current.pop()
    bk(0,[])
    return result

print(subSet([1,2,3]))
