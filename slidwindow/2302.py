"""
The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.
"""

def scoreS(arr,k):
    left = 0
    count = 0
    sm = 0
    for right in range(len(arr)):
        sm+=arr[right]
        while sm*(right-left+1) >=k:
            sm-=arr[left]
            left+=1
        count+=(right-left+1)
    return count

test_case = [[[2,1,4,3,5],10]]
for a, k in test_case:
    print(scoreS(a,k))








