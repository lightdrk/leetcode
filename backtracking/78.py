def subsets(nums):
    length = len(nums)
    output = []
    def bk(tmp,start):
        output.append(tmp[:])
        for i in range(start,length):
            tmp.append(nums[i])
            bk(tmp,i+1)
            tmp.pop()
    bk([],0)
    return output

print(subsets([1,2,3]))
