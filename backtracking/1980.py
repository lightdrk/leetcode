'''
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

'''
test_case = [["01","10"],["00","01"],["111","011","001"]]


def unique(nums):

    l = len(nums[0])
    nums = set(nums)
    ans = ['']
    def bk(i,s):
        if ans[0]:
            return 
        if i >= l:
            if not s in nums:
                ans[-1] = s
            return
        bk(i+1, s+'0')
        bk(i+1, s+'1')
    bk(0,'')
    return ans[0] 

def unique_v1(nums):
    l = len(nums[0])
    nums = set(nums)
    ans = []
    def bk(i,s):
        if i >= l:
            ans.append(''.join(s))
            return 
        s[i] = '1'
        bk(i+1,s)
        s[i]='0'
        bk(i+1,s)

    bk(0,['0']*l)
    return ans
for t in test_case:
    print(unique(t))
    print(unique_v1(t))























