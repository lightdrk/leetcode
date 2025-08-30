'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

variation if sum <= k then ?
    '''
def func(arr,k):
    def counting(k):
        hash_map = {0:1}
        prefix = 0
        ans = 0
        for n in arr:
            prefix+=n
            if prefix-k in hash_map:
                    ans+=hash_map[prefix-k]

            hash_map[prefix] = hash_map.get(prefix,0)+1
        return ans
    last = min(arr)

    return sum(counting(i) for i in range(k,last-1,-1))



edge = [[[1,1,1],2], [[12,13,14],1], [[1],1]]


for array,k in edge:
    print(func(array,k))


'''
need advanced data strucutreu liek binary indexed tree, or segment tree etc i dont know about it but can be asked above question will be asked may be for check out what i know


'''
