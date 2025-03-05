def fourSum(nums: list[int], target: int):
    length = len(nums)
    if length < 4:
        return []
    output = []
    nums.sort()
    for i,n in enumerate(nums):
        if i>0 and nums[i-1] == n:
            continue
        for idx in range(i+1,length):
            nx = nums[idx]
            left = idx+1
            right = length-1
            while left < right:
                sm = n + nx + nums[left] + nums[right]
                if sm == target:
                    output.append([n,nx,nums[left],nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                elif sm > target:
                    right-=1
                else:
                    left+=1

    return output


print(fourSum([1,0,-1,0,-2,2],0))
print(fourSum([2,2,2,2],8))
