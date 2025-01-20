def combination(nums :list[list], target :int) ->list[list]:
    length = len(nums)
    output = []
    def bk(curr, start):
        total = 0
        for i in curr:
            total+=nums[i]
            if total == target:
                if not curr in output:
                    output.append(curr)
            elif total > target:
                return
        for i in range(start,length):
            curr.add(i)
            bk(curr, i+1)
            curr.remove(i)
    bk([],0)
    return output

print(combination([1,2,3,4,5], 6))
print(combination([10,1,2,7,6,1,5],8))
print(combination([2,3,6,7], 7))

