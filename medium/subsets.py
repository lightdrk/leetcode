def sub(nums):
    output = []
    nums.sort()
    length = len(nums)
    def bk(curr, start):
        output.append(curr[:])
        for i in range(start,length):
            if i > start and nums[i] == nums[i-1]:
                continue
            curr.append(nums[i])
            bk(curr, i+1)
            curr.pop()
    bk([],0)
    return output

print(sub([1,2,2]))
