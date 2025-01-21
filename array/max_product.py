def m(nums):
    nums.sort()
    return max(nums[0]*nums[1], nums[len(nums)-1]*nums[len(nums)-2])
print(m([1, 3, 5, 2, 8]))
print(m([-10,-20,5,2,8]))
print(m([-5,-2,-3,-8]))
print(m([7,7,7,7]))



