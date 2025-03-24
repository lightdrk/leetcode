def minimumDifference(nums: list[int], k: int) -> int:
    length = len(nums)
    if length < 2:
        return 0
    nums.sort()
    print(nums)
    curr = nums[k-1] - nums[0]
    min_diff = curr
    for i in range(k,length):
        print(i-k+1)
        curr = nums[i] - nums[i-k+1]
        print('curr diff ->',curr)
        if min_diff > curr:
            min_diff = curr
    return min_diff

print(minimumDifference([9,4,1,7], 2))
