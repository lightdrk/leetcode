'''
Problem 1:
You are given an array of integers. Find the length of the longest subarray with sum equal to 0.

Example:
text
Copy
Edit
Input: [1, 2, -3, 3, -1, -2, 4]
Output: 5  
Explanation: The subarray [2, -3, 3, -1, -2] has sum 0 and length 5.


'''

def func(arr: list[int]):
    count = 0
    l = len(arr)
    for i in range(l):
        sm = 0
        for j in range(i,l):
            if sm == 0:
                count = max(count, j-i)
            sm+=arr[j]

    return count

def func2(arr: list[int]) ->int:
    l = len(arr)
    prefix = []
    sm = 0
    for a in arr:
        sm+=a
        prefix.append(sm)
    print(prefix)
    return 0

test_case = [[1, 2, -3, 3, -1, -2, 4],[0,0,0,0,0,0,0,0], [1,-1,-1,1], [1], [1,2,3]]

for t in test_case:
    print(func(t))

func2(test_case[0])
