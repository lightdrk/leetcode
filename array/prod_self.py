def self_prod(nums):
    length =len(nums)
    output = [1]*length
    prefix = 1
    for i in range(length):
        output[i] = prefix
        prefix = nums[i]*prefix
    sufix = 1
    for i in range(length-1,-1,-1):
        output[i]*=sufix
        sufix*=nums[i]
    print(output)




print(self_prod([1,2,3,4]))
print(self_prod([0,2,3,4]))
