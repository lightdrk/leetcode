def minSub(target, nums):
    length = len(nums)
    left = 0 
    right = 0 
    count = float('inf')
    sm = 0
    for right in range(length):
        sm+=nums[right]
        while sm >= target:
            count = min(count, right-left+1)
            sm-=nums[left]
            left+=1

    return count if count != float('inf') else 0 
print(minSub(7,[2,3,1,2,4,3]))
