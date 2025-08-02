'''
    🔷 Problem: Count Number of Nice Subarrays

You are given an integer array nums and an integer k.
A nice subarray is a contiguous subarray that contains exactly k odd numbers.

Return the number of nice subarrays.

'''

def func(arr, k):
    l = len(arr)
    if l < k:
        return 0
    odd = 0
    left = 0
    count = 0
    for right in range(l):
        print('odd->',odd, count)
        if arr[right]&1 == 1:
            odd+=1
        while odd > k:
            if arr[left]&1 == 1:
                odd-=1
            left+=1
        while odd == k:
            count+=1
            if arr[left]&1 == 1:
                break
            left+=1

    return count

test = [([1,2,1,1,4],3),([1,2,3],2), ([1,2,2,3],1), ([1,1,1,1],1), ([1,1,1],3)]
'''
couldnt reach answer beacuse it does not work on [2,2,2,3,2,3,3,2,2]
will not work on this whole as it breaks after getting odd = 3 we start decreasing it makingit so left never 0 
'''
for arr, k in test:
    print(func(arr,k))

