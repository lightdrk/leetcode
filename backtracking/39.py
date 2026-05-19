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


test_case = [[[1,2,3,4,5,6,7],7], [[1,2,3,4,5,6],10], [[2,3,6,7],7]]


def comination(nums,target):
    output = []
    l = len(nums)
    def bk(s,arr,i):
        if s == target:
            output.append(arr[:])
            return
        if s > target:
            return
        for ni in range(i,l):
            arr.append(nums[ni])
            bk(s+nums[ni],arr,ni)
            arr.pop()
    bk(0,[],0)
    return output

for n,t in test_case:
    print(comination(n,t))
