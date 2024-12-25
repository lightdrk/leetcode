def binary(nums,v):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left + (right - left) //2
        if nums[mid] == v:
            return mid
        if nums[mid] > v:
            right=mid-1
        else:
            left=mid+1

print(binary([1,2,3,4],1))

