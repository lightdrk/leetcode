"""
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)]


"""


def resultsArray(nums,k):
    l = len(nums)
    power = [-1]*(l-k+1)
    left = 0
    for right in range(1,l):
        if right-left+1 == k:
            break
        if nums[right] < nums[right-1]:
            left = right

