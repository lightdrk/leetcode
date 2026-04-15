'''
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.
'''

test_case = [[[1,2,3,1],3,0],[[1,5,9,1,5,9],2,3],[[1,2,2,3,4,5],3,0]]

def dups(nums,i,v)->bool:
    left = 0
    for right in range(1,len(nums)):
        if right-left>i:
            left+=1
        tmp = left
        while tmp<right:
            if abs(nums[right]-nums[tmp]) <= v:
                return True
            tmp+=1

    return False

def dupsV1(nums,i,v)->bool:
    left = 0

    for right in range(1,len(nums)):
        if right-left>i:
            left+=1
        tmp = left
        while tmp<right:
            if abs(nums[right]-nums[tmp]) <= v:
                return True
            tmp+=1

    return False


for t,i,v in test_case:
    print(dups(t,i,v))

import bisect

def t1(arr,i,v):
    left = 0
    window = []
    for right in range(len(arr)):
        r = bisect.bisect_right(window,arr[right])

















