nums = [3,1,5]
for mask in range(1<<len(nums)):
    for i in range(len(nums)):
        if mask & (1<<i):
            print(nums[i])

