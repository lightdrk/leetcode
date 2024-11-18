'''
Subarray With Maximum Average Length Greater Than k
Given an integer array nums and an integer 𝑘
k, find a contiguous subarray with length greater than or equal to 𝑘
k that has the maximum average value and return this value.
'''
def maxAverLength(nums :List [int], k :int)-> int:
    curr = sum(nums[:k])
    max_sum = curr
    for i in range(k, len(nums)):
        curr = curr + nums[i]
        if max_sum < curr:

    return max_sum


