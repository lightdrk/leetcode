'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

'''
'''
def func(arr: list, k: int):
    count = 0 
    prefix = 0
    for n in arr:
        prefix+=n
        if prefix == k
'''

def func(arr):
    sub = []
    b = []
    l = len(arr)
    for i in range(l):
        prev = []
        for j in range(i,l):
            print(arr[j])
            b.append(arr[i:j+1])
            prev.append(arr[j])
            sub.append(prev[:])
        print(sub)


    return b

test_case = [([1,2,3,4,5],15)]
for t,l in test_case:
    print(len(func(t)) == l)

def Ofunc(arr,k):
    count = 0
    prefix = 0
    hash_map = {}
    h = {}
    for i in range(len(arr)):
        prefix+=arr[i]
        if prefix == k:
            count+=1
            print(arr[:i+1])
        if prefix-k in hash_map:
            count+=hash_map[prefix-k]
            print(arr[h[prefix-k]+1:i+1])

        if prefix not in h:
            h[prefix] = i
        hash_map[prefix] = hash_map.get(prefix,0)+1
    return count

#print(Ofunc([3,4,7,2,-3,1,4,2],7))
#
#print(Ofunc([0,0,0],0))
#print(Ofunc([1,2,3],3))
print(Ofunc([0,-1,0,-1],-1))
print(Ofunc([1,2,1,2,1],3))
print(Ofunc([1,2,3],2))

'''
modified version if we want to get sub array itself then ? not the count direct subarray

'''
def OOfunc(arr,k):
    prefix = 0
    output = []
    hash_map = {0: [-1]}
    for i in range(len(arr)):
        prefix+=arr[i]
        if prefix-k in hash_map:
            for j in hash_map[prefix-k]:
                output.append(arr[j+1:i+1])
        if prefix not in hash_map:
            hash_map[prefix] = []
        hash_map[prefix].append(i)
    return output

print(OOfunc([0,-1,0,-1],-1))
print(OOfunc([1,2,1,2,1],3))
print(OOfunc([1,2,3],2))
print(OOfunc([3, 4, -7, 1, 2, -6, 1, 1, 1],0))

