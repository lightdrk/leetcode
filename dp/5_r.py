'''
Given a string s, return the longest palindromic substring in s.
'''
from functools import cache

def q(s: str):
    l = len(s)
    print(l)
    def dp(left,right):
        while left> -1 and right < l and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    ans = ''
    for i in range(l):
        a = dp(i,i)
        b = dp(i,i+1)
        ans = max(ans,a,b,key=len)
    return ans
def qq(s: str):
    l = len(s)
    print(l)
    @cache
    def dp(left,right):
        if left < 0 or right >= l or s[left] != s[right]:
            return s[left+1:right]
        return dp(left-1,right+1)
    ans = ''
    for i in range(l):
        a = dp(i,i)
        b = dp(i,i+1)
        ans = max(ans,a,b,key=len)
    return ans

print(q('abbannnda'))
print(qq('abbannnda'))
