def unique(nums):
    k = 1
    length = len(nums)
    for i in range(1,length):
        if nums[i] > nums[i-1]:
            nums[k] = nums[i]
            k+=1

    return k


l = [1,1,2]
print(unique(l))

print(l)
