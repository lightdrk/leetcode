def subSeq(nums):
    length = len(nums)
    memo = {}
    def recur(i):
        if i >= length:
            return 0
        if i in memo:
            return memo[i]
        ans = 0
        for idx in range(i+1,length):
            #print(idx, nums[idx])
            if nums[i] < nums[idx]:
                #print(recur(idx))
                ans = max(ans, 1+recur(idx))
        memo[i] = ans
        return ans
    
    return 1+ max(recur(i) for i in range(length))


print(subSeq([10,9,2,5,3,7,101,18]))
print(subSeq([1,2,3,4,5,6,7]))
print(subSeq([0,1,0,3,2,3]))
print(subSeq([0,0,0,0,0,0]))


