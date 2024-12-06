def bt(nums,t,n):
    if t == 0:
        return True
    if n == 0:
        return False

    if nums[n-1] > t:
        return bt(nums,t,n-1)

    return bt(nums,t-nums[n-1], n-1) or bt(nums, t, n-1)

def subSum(nums, target):
    if not nums:
        return False
    return bt(nums,target,len(nums))


print(subSum([3,34,4,12,2],10))
