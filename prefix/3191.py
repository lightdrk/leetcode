def minOp(nums:list)->int:
    flips = 0
    zero = nums[:3].count(0)
    for left in range(len(nums)-2):
        if nums[left] == 0:
            flips+=1
            nums[left] = 1
            nums[left+1] ^=1
            nums[left+2]^=1
            left +=1
    return flips if 0 not in nums else -1 


    print(zero)
    if zero == 0:
        return -1
    return flips

testCase = [[0,1,1,1,0,0]]
for test in testCase:
    print(minOp(test))
