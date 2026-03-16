'''
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

'''
from collections import defaultdict

test_case = [[1,1,3,2,3,2,2],[1,1,1,1],[0,0,1,2,3,0]]

def func(nums):
    unique = len(set(nums))
    hash_map = {}
    l = len(nums)
    distinct = 0
    left = 0 
    count = 0
    for right in range(l):
        if not nums[right] in hash_map:
            distinct+=1
            hash_map[nums[right]] = 0
        hash_map[nums[right]]+=1
        while distinct == unique:
            count+=(l-right)
            hash_map[nums[left]]-=1
            if hash_map[nums[left]] == 0:
                distinct-=1
                hash_map[nums[left]]-=1
            left+=1
    return count 

for t in test_case:
    print(func(t))



































