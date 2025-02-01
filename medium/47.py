def permute(nums):
    length = len(nums)
    output = []
    nums.sort()
    def bk(idx):
        if idx == length:
            output.append(nums[:])
        for i in range(idx,length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums[i],nums[idx] = nums[idx], nums[i]
            bk(idx+1)
            nums[i],nums[idx] = nums[idx], nums[i]
    bk(0)
    return output
print(permute([1,1,2]))
