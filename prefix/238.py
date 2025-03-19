def product(nums):
    length = len(nums)
    output = [1]*length
    fix = 1
    for i in range(length):
        output[i] = fix
        fix*= nums[i]
    fix = 1
    for i in range(length-1, -1, -1):
        output[i]*=fix
        fix*=nums[i]
    print(output)
product([1,2,3,4])
