#def mxSub(nums):
#    length = len(nums)
#    def recur(i,ans):
#        if i >= length:
#            return 0
#
#        return max(ans, recur(i+1,ans+nums[i]), recur(i+1,nums[i]))
#
#    return recur(0,0)
#
#print(mxSub([-2,1,-3,4,-1,2,1,-5,4]))
#
#print(mxSub([1]))
#print(mxSub([5,4,-1,7,8]))

'''
def mxSub(nums):
    ans = float('-inf')
    length = len(nums)
    for i in range(length):
        for j in range(i,length):
            ans = max(ans, sum(nums[i:j]))

    return ans
'''
from functools import cache

def mxSub(nums):
    l = len(nums)
    @cache
    def dp(idx):
        if idx >= l:
            return  float('-inf')
        return max(nums[idx]+dp(idx+1),nums[idx])
    return max(dp(i) for i in range(l))

print(mxSub([-2,1,-3,4,-1,2,1,-5,4]))

print(mxSub([1]))
print(mxSub([5,4,-1,7,8]))
