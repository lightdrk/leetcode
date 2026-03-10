test_case = [[0,1,1,1,1,1],[0,1,0,1,0,0,0],[0,1,1,1,0,0]]


def minOperations(nums):
    count = 0
    l = len(nums)
    for i in range(len(nums)-2):
        if nums[i] == 1:
            continue
        nums[i] = 1
        nums[i+1] ^=1
        nums[i+2] ^=1
        count +=1

    return count if not 0 in nums[l-2:] else -1


for t in test_case:
    print(minOperations(t))
