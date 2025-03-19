def mx_sm(arr, k):
    max_sm = sum(arr[0:k])
    length = len(arr)
    curr = max_sm
    for i in range(k,length):
        curr = curr-arr[i-k]+arr[i]
        if max_sm < curr:
            max_sm = curr
    return max_sm


test_cases = [
    [[2, 1, 5, 1, 3, 2], 3, 9],
    [[1, 2, 3, 4, 5], 2, 9],
    [[2, 3, 1, 5, 6, 7, 2], 4, 20],
    [[1, 2, 3], 1, 3],
    [[3, 1, 4, 1, 2], 3, 8],
    [[10, 5, 1, 2, 6], 4, 18],
    [[5, 5, 5, 5], 2, 10],
    [[1, 1, 1, 1, 1], 3, 3],
    [[5, 10, 15, 20, 25], 5, 75],
    [[1, 100, 2, 200, 3, 100, 4], 4, 307],
    [[1, 2, 3, 4], 4, 10],
    [[-1, -2, -3, -4], 2, -3]
]

for arr,k,ans in test_cases:
    print(mx_sm(arr,k) == ans)

