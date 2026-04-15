"""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array."""

test_case = [[[1,3,2,3,3],0]]

def countSub(arr,k):
    mx = max(arr)
    count = 0
    left = 0
    ans = 0
    l = len(arr)
    for right in range(l):
        if arr[right] == mx:
            count+=1
        while count >= k and left<=right:
            if mx == arr[left]:
                count-=1
            ans+=(l-right)
            left+=1
    return ans


for a,k in test_case:
    print(countSub(a,k))









