def leftRightDiff(nums: list):
    l = len(nums)
    prefix = [nums[0]]*l
    for i in range(1,l):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix

print(leftRightDiff([10,4,8,3]))

