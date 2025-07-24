'''

You are given a 0-indexed array nums consisting of positive integers.

You can do the following operation on the array any number of times:

Choose an integer i such that 0 <= i < nums.length - 1 and nums[i] <= nums[i + 1]. Replace the element nums[i + 1] with nums[i] + nums[i + 1] and delete the element nums[i] from the array.
Return the value of the largest element that you can possibly obtain in the final array.


'''

def maxArrayValue(nums: list[int]):
    output = -1
    prev = 0
    i = len(nums)-1
    while i > -1:
        curr = nums[i]
        if prev >=curr:
            prev+=curr
        else:
            prev = curr
        output = max(output,prev)
        i-=1
    return output

print(maxArrayValue([7]))
print(maxArrayValue([1,2,5,2,6]))
print(maxArrayValue([1,2,1,17,8]))
print(maxArrayValue([7,6,4,3,2]))
