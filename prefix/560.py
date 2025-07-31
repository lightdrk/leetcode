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
