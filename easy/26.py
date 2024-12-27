def rmdups(nums):
    a = 0
    length = len(nums)
    for j in range(1,length):
        if nums[a] != nums[j]:
            a+=1
            nums[a] = nums[j]
    print(a)
nums = [1,1,1,2,2,3,4,4,5,5,5,6]

rmdups(nums)
print(nums)

