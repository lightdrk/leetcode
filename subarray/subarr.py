
def subarr(nums):
    if len(nums) == 1:
        return [nums]
    possible = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            possible.append(nums[i:j])
    return possible

print(subarr('abcabcbb'))

possiblity = []
def recurSub(nums, start, end):
    if start >= end:
        return
    if start < end:
        recurSub(nums, start+1, end)

    possiblity.append(nums[start:end])
    if end > start:
        recurSub(nums, start, end-1)



recurSub([1,2,3,4],0,4)
print(possiblity)
