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

test = [([1,2,1,1,4],3),([1,2,3],2), ([1,2,2,3],1), ([1,1,1,1],1), ([1,1,1],3), ([2,2,2,3,2,3,3,2,2,2],3)]
'''
couldnt reach answer beacuse it does not work on [2,2,2,3,2,3,3,2,2]
will not work on this whole as it breaks after getting odd = 3 we start decreasing it makingit so left never 0 
'''
for arr, k in test:
    print(func(arr,k))


'''
due to some guys comment , if we convert the whole array in to 1 and zero where 1 is for odd and 0 for even then promblem becomes , find the sub arrays where some of sub array equal to k ,, like i have done previously 

[0,0,0,1,0,1,1,0,0]
here prefix will be 3 on idx 6 
hash_map {0:-1,0,1,2}
hash_map {1:3}
hash_map {2: 5}
count = 4
we can add the len of array at 0 tocount 
{3:6}
count = 8
count = 12

correct answer
    '''

def funcPrefix(arr,k):
    prefix = 0
    hash_map = {0:1}
    count = 0
    for n in arr:
        if n&1 == 1:
            prefix +=1
        if prefix-k in hash_map:
            count+=hash_map[prefix-k]
        hash_map[prefix] = hash_map.get(prefix,0) + 1

    return count

for arr, k in test:
    print(funcPrefix(arr,k))
