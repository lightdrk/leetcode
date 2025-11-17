'''
1. Square Root Ceiling

Given an integer n, find the smallest integer x such that
x*x >= n.
'''

'''
 4, --> 2
1 ? 
'''
def ans(n):
    left = 1
    right = n
    while left < right:
        mid = left + (right-left)//2
        if mid*mid < n:
            left = mid+1
        else:
            right = mid
    return left

test_case = [3,2,4,5,6,7,8,9,121,122,100]

for t in test_case:
    print(ans(t))
