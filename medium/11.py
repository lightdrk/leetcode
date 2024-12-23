def maxArea(nums):
    max_area = 0
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] < nums[right]:
            max_area = max(max_area, (nums[left]) * (right - left))
            left = left + 1
        else:
            max_area = max(max_area, nums[right] * (right-left))
            right = right - 1
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
