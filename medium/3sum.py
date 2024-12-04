def threeSum(nums):
    nums.sort()
    result = []
    length = len(nums)
    for i in range(length):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = length - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left = left + 1
                right =  right -1
                # this will remove duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left = left + 1
                #we can also have this for right but not needed as any of one side dups
                #are removed they become unique
            elif total > 0:
                right = right - 1
            else:
                left = left + 1
    return result

print(threeSum([-1,0,1,2,-1,-4]))
