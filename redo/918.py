'''

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
'''

def mx(arr):
    l = len(arr)
    i = 0
    j = 1
    ans= run = arr[0]
    while j!=i:
        if arr[j%l] >= arr[j%l]+run:
            run = arr[j%l]

        else:
            run = arr[j%l]+run

        j+=1


