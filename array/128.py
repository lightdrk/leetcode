def longestConsecutive(nums: list[int]) -> int:
    nums = set(nums)
    con = 0
    for n in nums:
        r = 0
        print(n)
        while n in nums:
            print(n)
            print()
            r+=1
            n+=1
        if con < r:
            con  = r
    return con
#print(longestConsecutive([1,5,4,3,2,1,1]))

print(longestConsecutive([100,4,200,1,3,2]))
#print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
#print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
