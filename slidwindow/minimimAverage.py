'''
Given an integer array nums and an integer 𝑘
k, find a contiguous subarray of length 𝑘
k that has the minimum average value and return this value.
'''
def minAverage(nums, k):
    curr = sum(nums[:k])
    min_sum = curr
    for i in range(len(nums)-k):
        curr = curr -  nums[i] + nums[i+k]
        min_sum = min(min_sum, curr)
    return min_sum/k

test_case = [
    ([3, 7, 5, 2, 8, -1, 6, 4], 3),  # Expected Output: 3.0
    ([1, -2, 3, 5, -6, 7, 1], 2),  # Expected Output: -2.5
    ([4, 6, 2, 9, 5, 1], 4),  # Expected Output: 5.0
    ([10, 20, 30, 40, 50], 2),  # Expected Output: 15.0
    ([-1, -3, -2, -4, -5], 3),  # Expected Output: -4.0
]

for i in test_case:
    print(f'{i[0]},{i[1]} ==> {minAverage(i[0], i[1])}')
