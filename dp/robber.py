def rob(nums):
    #first approact wrong dosent look for if not going n+2 we go n+3 
    # can not rob adjecent not it doesnt say only rob adjecent remember
    #[1,2,3,1]
    #1, 2
    # n + n+2

    a = nums[0]
    b = nums[1]
    #n = n-1 or n + 1
    for i in range(2,len(nums)):
        curr = a + nums[i]
        a = b
        b = curr
    return max(a,b)

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([2,1,1,2]))

def realRob(nums):
    rob1,rob2 = 0, 0
    for n in nums:
        curr = max(rob1+n, rob2)
        rob1 = rob2
        rob2 = curr
    return rob2

print(realRob([1,2,3,1]))
print(realRob([2,7,9,3,1]))
print(realRob([2,1,1,2]))


