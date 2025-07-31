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
            sm+=arr[j]
            if sm == 0:
                count = max(count, j-i +1)
    return count

def func2(arr: list[int]) ->int:
    sm = 0
    count = 0
    seen = {}
    for i,a in enumerate(arr):
        sm+=a
        if sm == 0:
            count = i+1
        if sm in seen:
            count = max(count, i-seen[sm])
        else:
            seen[sm] = i
    return count

test_case = [[1, 2, -3, 3, -1, -2, 4],[0,0,0,0,0,0,0,0], [1,-1,-1,1], [1], [1,2,3]]

for t in test_case:
    print(func(t))
    print(func2(t))
