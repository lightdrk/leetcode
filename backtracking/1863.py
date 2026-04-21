'''
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

 
'''
test_case = [[5,1,6],[3,4,5,6,7,8],[0,1,2]]

def subSetXOR(nums):
    l = len(nums)
    arr = []
    def subset(i,ans):
        if i >= l:
            arr.append(ans)
            return
        subset(i+1,ans^nums[i])
        subset(i+1,ans)
    subset(0,0)
    print(sum(arr))


for t in test_case:
    subSetXOR(t)
