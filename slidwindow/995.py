"""

You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

"""
test_case = [[[0,1,0],1],[[0,0,0,1,0,1,1,0],3], [[1,1,0],2],[[1,1,1,1,1,1],1]]

'''

k >= 1

'''
from collections import deque

def minKBitFlips(nums,k):
    left = 0
    flip = 0
    zero = deque()
    one = deque()
    for i in range(k):
        if nums[i] == 0:
            zero.append(i)
            continue
        one.append(i)

    for right in range(k,len(nums)):
        if zero and (left in zero):
            flip+=1
            zero,one = one,zero
        if one:
            one.popleft()
        left+=1
        if nums[right] == 0:
            zero.append(right)
            continue
        one.append(right)
    if left in zero:
        flip+=1
        zero,one = one,zero
    if zero:
        return -1
    return flip


for nums,k in test_case:
    print(minKBitFlips(nums,k))


"""
        left = 0
        flip = 0
        zero = set()
        one = set()
        for i in range(k):
            if nums[i]:
                one.add(i)
                continue
            zero.add(i)

        for right in range(k,len(nums)):
            if left in zero:
                flip+=1
                zero,one = one ,zero
            one.remove(left)
            left+=1
            if nums[right] == 0:
                zero.add(right)
                continue
            one.add(right)
        if left in zero:
            flip+=1
            zero,one = one,zero
        if zero:
            return -1
        return flip

"""
