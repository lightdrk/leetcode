'''
Consider the array as circular, meaning the last element wraps around to the first element. Find a contiguous subarray of length 
𝑘
k that has the maximum average value.

Problem Statement:
Given a circular array nums and an integer 
𝑘
k, find a contiguous subarray of length 
𝑘
k that has the maximum average value.
'''

def circular(nums: list[int], k: int) -> float:
    n = len(nums)
    sum_of = sum(nums[:k])
    av = sum_of
    for i in range(1, n):
        sum_of = sum_of - nums[i-1] + nums[(i+k-1)% n]
        av = max(av, sum_of)
    return av/k
print(circular([5, 1, 3, 7, 2], 2))
print(circular([7, 7, 7, 7, 7], 3))
print(circular([5, -1, 3, -2, 8], 3))
print(circular([1, 1, 1, 1000, 1], 3))
print(circular([1, 100, 1, 100, 1, 100], 2))
print(circular([i for i in range(1, 1000001)], 1000))
