test_case = [[1,1,1,2,2,3],[1,2,3,4], [1,1,1,1,1,1,2,2],[1]]
def removeDups(nums):
    slow = 0
    i = 0
    l = len(nums)
    if l == 1:
        return slow
    if nums[0] == nums[1]:
        slow+=1
    i = slow
    while i < l:
        if nums[slow] != nums[i]:
            slow+=1
            nums[slow]=nums[i]
            if i+1 < l and nums[i] == nums[i+1]:
                slow+=1
                i+=1
                nums[slow] = nums[i]
        i+=1
    return slow


for t in test_case:
    print('pointer ->',removeDups(t))
    print(t)

#above works if we are talking about we can have atmost two , but if this atmost two becomes dynamic then 
def removeDupsK(nums,k):
    slow = 0
    i = 0
    l = len(nums)
    if l == 1:
        return slow
    r = 0
    while slow < l -1 and nums[slow] == nums[slow+1] and r<k:
        slow+=1
        r+=1
    i = slow
    while i < l:
        if nums[slow] != nums[i]:
            slow+=1
            nums[slow]=nums[i]
            r = 0
            while i+1 < l and nums[i] == nums[i+1] and r < k:
                slow+=1
                i+=1
                r+=1
                nums[slow] = nums[i]
        i+=1
    return slow

for t in test_case:
    print(removeDupsK(t,2))
    print(t)
