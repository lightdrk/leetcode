def num(nums, goal):
    left = 0
    count = 0
    sm = 0
    length = len(nums)
    for right in range(length):
        sm+=nums[right]
        while sm >= goal and left <= right:
            if sm == goal:
                count+=1
            if sm-nums[left] < goal:
                break
            sm-=nums[left]
            left+=1

    return count

print(num([1,0,1,0,1], 2))
print(num([0,0,0,0,0], 0))
