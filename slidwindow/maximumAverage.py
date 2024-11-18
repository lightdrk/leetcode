'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

'''

def maxAverage(nums, k):
    curr = sum(nums[:k])
    maxSum = curr
    for i in range(len(nums)-k):
        curr = curr - nums[i] + nums[i+k]
        maxSum = max(maxSum, curr)
    return maxSum / k


print(maxAverage([1,12,-5,-6,50,3], 4))


