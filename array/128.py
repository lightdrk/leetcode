def longestConsecutive(nums: list[int]) -> int:
    start = float('inf')
    new = {}
    for n in nums:
        if start > n:
            start = n
        if not n in new:
            new[n] = 0
        new[n]+=1
    consecutive = 0
    while start in new:
        consecutive+=1
        if not new[start]:
            consecutive-=1
            start+=1
        else:
            new[start]-=1
    return consecutive

print(longestConsecutive([1,5,4,3,2,1,1]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
