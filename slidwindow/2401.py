"""
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

"""
test_case = [[3,1,8,48,10, 3,8,48],[3,1,5,11,13], [84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680]]

def longestNiceSub(nums):
    left = 0
    output = 1
    mask = nums[0]
    for right in range(1,len(nums)):
        while mask&nums[right] != 0 and left<right:
            mask ^= nums[left]
            left+=1
        mask|=nums[right]
        if output < (right-left+1):
            output = right-left+1
    return output


for t in test_case:
    print(longestNiceSub(t))
