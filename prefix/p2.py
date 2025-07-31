'''
🔸Problem: Longest Subarray with Sum K

Given an array of integers arr and an integer k, return the length of the longest subarray that sums to k.

1 <= len(arr) <= 10^5

-10^4 <= arr[i] <= 10^4

-10^9 <= k <= 10^9

'''

#brute force is double for loop here
#optimized with prefix sum with seen hash_map
def func(arr: list[int], k:int) -> int:
    prefix = 0
    count = 0
    seen = {}
    for i, a in enumerate(arr):
        prefix+=a
        if prefix == k:
            count = i+1
        if prefix-k in seen:
            count = max(count, i-seen[prefix-k])
        if prefix not in seen:
            seen[prefix] = i

    return count
test = [([10, 5, 2, 7, 1, 9],15), ([1,2,3],3), ([5,10], 15), ([-1,-1,1,2,3], 4), ([3,1,-1,2,5,-3],0), ([1,2,3], 7),([1,2,3,-3,4],3)]

for t, k in test:
    print(func(t,k))

print(func([3,1,-1,2,5,-3],6))
