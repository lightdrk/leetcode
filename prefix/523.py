'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of


'''
def func(arr, k):
    if k == 0:
        return False
    prefix = 0
    hash_map = {0:-1}

    for i,n in enumerate(arr):
        prefix+=n
        modulo = prefix%k
        if modulo in hash_map and i - hash_map[modulo]:
            return True
        if modulo not in hash_map:
            hash_map[modulo] = i

    return False


'''
above works for 0 to .. positive int , but what about neg int

'''
def funcv2(arr,k):
    #arr can be negative so k == 0 condition is invalid

    prefix = 0
    hash_map = {0:-1}
    if k == 0:
        for i , n in enumerate(arr):
            prefix+=n
            if prefix in hash_map and i - hash_map[prefix] >1:
                return True
            if prefix not in hash_map:
                hash_map[prefix] = i
        return False
    for i,n in enumerate(arr):
        prefix+=n
        modulo = prefix%k
        if modulo in hash_map and i - hash_map[modulo] > 1:
            return True
        if modulo not in hash_map:
            hash_map[modulo] = i
    return False

test = [([-1,-1,2],-1), ([-23,-2,-4],6), [(-1,4,3),6], ([-1,-1,2],0)]
for arr,k in test:
    print(funcv2(arr,k))


'''
then what about getting the array them selves
'''

def funcv3(arr,k):
    #arr can be negative so k == 0 condition is invalid

    prefix = 0
    output = []
    hash_map = {0:[-1]}
    if k == 0:
        for i , n in enumerate(arr):
            prefix+=n
            if prefix in hash_map:
                for j in hash_map[prefix]:
                    if i - j > 1:
                        output.append(arr[j+1:i+1])
            if prefix not in hash_map:
                hash_map[prefix] = []
            hash_map[prefix].append(i)
        return output
    for i,n in enumerate(arr):
        prefix+=n
        modulo = prefix%k
        if modulo in hash_map:
            for j in hash_map[modulo]:
                if i-j > 1:
                    output.append(arr[j+1:i+1])
        if modulo not in hash_map:
            hash_map[modulo] = []
        hash_map[modulo].append(i)
    return output

test = [([-1,-1,2],-1), ([-23,-2,-4],6), [(-1,4,3),6], ([-1,-1,2],0), ([0,0,0],0)]
for arr,k in test:
    print(funcv3(arr,k))

