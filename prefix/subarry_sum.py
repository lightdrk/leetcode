def sumArray(arr, k):
    length = len(arr)
    count = 0
    for i in range(length):
        current = 0
        for right in range(i,length):
            current+=arr[right]
            if current == k:
                count+=1
    return count


test_cases = [
    [[[1, 1, 1], 2], 2],    # Subarrays [1, 1] and [1, 1] both sum to 2
    [[[1, 2, 3], 3], 2],    # Subarrays [1, 2] and [3] sum to 3
    [[[1, 2, 3, 4], 5], 2], # Subarrays [2, 3] and [1, 2, 3] sum to 5
    [[[0, 0, 0, 0], 0], 10], # There are 10 subarrays that sum to 0
    [[[-1, -1, 1], 0], 2],  # Subarrays [-1, -1] and [1] sum to 0
    [[[1, -1, 0], 0], 2],   # Subarrays [-1, 1] and [0] sum to 0
    [[[], 3], 0],           # Empty array, no subarrays to sum to 3
    [[[1, 2, 3], 6], 1],    # Only one subarray [1, 2, 3] sums to 6
    [[[1, -1, 2, 3], 4], 2], # Subarrays [1, -1, 2, 3] and [-1, 2, 3] sum to 4
    [[[1, 2, 3], 7], 0]     # No subarray sums to 7
]

for [arr, k], ans in test_cases:
    print(arr,k,ans)
    result = sumArray(arr, k)
    print( f'{result} == {ans}',result == ans)

