'''

You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

If the pile is not empty, remove the topmost element of the pile.
If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.


    '''


test_cases = [([9,1,2,7],2), ([9,1,10,2,7],2), ([9,10,3,2,5],2), ([9,1],2), ([1],2), ([3,2],1), ([8,1,2,3,10],3)]

'''
in complete do it later

        '''
def func(arr,k):
    l = len(arr)
    if l <= k:
        return -1
    if k == 1:
        return arr[1]
    pm = float('-inf')
    for i in range(k-2):
        pm = max(pm,arr[i])
    p2 = arr[k-2]
    p3 = 0
    if k+1 < l:
        p3 = arr[k]
    else: 
        p3 = float('-inf')
    return max(p2,p3,pm)


for arr,k in test_cases:
    print(func(arr,k))
