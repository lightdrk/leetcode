def permute(nums):
    length = len(nums)
    output = []
    def bk(i):
        if i == length-1:
            output.append(nums[:])
            return
        for j in range(i,length):
            nums[i],nums[j] = nums[j],nums[i]
            bk(i+1)
            nums[i],nums[j] = nums[j],nums[i]

    bk(0)
    return output

print(permute([1,2,3]))
