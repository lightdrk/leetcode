def prod(nums):
    length = len(nums)
    prefix = [0]*length
    pref = 1
    for i in range(length):
        prefix[i] = pref
        pref*=nums[i]
    pref = 1
    for i in range(length-1,-1,-1):
        prefix[i]*=pref
        pref*=nums[i]
    print(prefix)

prod([1,2,3,4])
prod([1,0,3,4])
