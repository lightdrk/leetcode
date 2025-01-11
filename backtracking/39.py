def combinatio_sum(nums,target):
    output = []
    length = len(nums)
    def bk(current,start):
        s=sum(current)
        if s == target:
            output.append(current[:])
        if s > target:
            return
        for i in range(start,length):
            current.append(nums[i])
            bk(current,i)
            current.pop()
    bk([],0)
    return output

print(combinatio_sum([2,3,6,7],7))
