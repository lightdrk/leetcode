def combination(nums :list[list], target :int) ->list[list]:
    nums.sort()
    print(nums)
    length = len(nums)
    output = []
    def bk(curr, start):
        total = sum(curr)
        if total == target:
            output.append(curr[:])
            return
        elif total > target:
            return
        for i in range(start,length):
            if i > start and nums[i-1] == nums[i]:
                continue
            if nums[i] > target:
                break
            curr.append(nums[i])
            bk(curr, i+1)
            curr.pop()
    bk([],0)
    output.sort()
    return output
print(combination([1,2,3],3))
print(combination([1,2,3,4,5], 6))
print(combination([10,1,2,7,6,1,5],8))
print(combination([2,3,6,7], 7))

