'''
    You are given a 0-indexed integer array nums, an integer modulo, and an integer k.

Your task is to find the count of subarrays that are interesting.

A subarray nums[l..r] is interesting if the following condition holds:

Let cnt be the number of indices i in the range [l, r] such that nums[i] % modulo == k. Then, cnt % modulo == k.
Return an integer denoting the count of interesting subarrays.

Note: A subarray is a contiguous non-empty sequence of elements within an array.
    '''

'''
OBSERVATIONS:
1. question is about getting the number of sub arrays that follow conditon given above like their module with modulo should be k || and || their lengts subarrays length %modulo === k

questions answer needed?
 1. here nums[i]%moudulo ==k does that mean every evelements modulo should be equal to k right?.
    soulution: prefix should be used here , but the problem above stands , 
        what happens? if we sum numbers with same modulo ? -> 1%2 == 1, 3%2 == 1, 5%2 here sums moudlo is also same lets test other cases, so  -> 1%4 then next same moudlo val will be 4+1, then 5+4 so to get next val with equal modulo , we do , the moudlo we want
        let say modulo we want it k then the moudlater will be modulo then -> k + modulo will give us that meaning add moudluo to previous


    ** sum of moudulo same modulo will have diff of moudulo itself, 
    ** what i have written , 
    ** another the other condition is that modulo based on the thing is number of same moudlo answers or k based
    '''
'''
1. what if we just make the array as binary, so 1 and 0 , where 1 will be that meets condition right , zero that does not ,as only cnt%modulo determines the answer here , we do not need sum or something.. 
if we do like (1 ) then we can simple do prefix sum , check where sum %moudlo is k then increase the count . i guess this is it , ..

    '''

test_cases = [([3,2,4],2,1,3),([1,2,3,4,5], 2,1,9),([2,2,2,2,2,2],2,1,0),([1,1,1],2,1,4),([1],2,1,1),([2],2,1,0)]

def func(arr,modulo,k):
    l = len(arr)
    hash_map = {0:1}
    count = 0
    prefix = 0
    for i in range(l):
        if arr[i]%modulo == k:
            prefix+=1
        rem = prefix%modulo
        count+= hash_map.get((rem-k+modulo)%modulo, 0)
        hash_map[rem] = hash_map.get(rem,0) + 1
    return count


for arr,m,k,a in test_cases:
    print(func(arr,m,k),a)
