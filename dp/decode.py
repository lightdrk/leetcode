from functools import cache
test_case = ["000000", "01", "1", "272", "1001", "1011"]

def func(s: str):
    l = len(s)
    d1 = 1
    d2 = 0 
    ans = 0
    for i in range(l-1,-1,-1):
        if s[i] == '0':
            ans = 0
        else:
            ans = d1
            if i+2 <= l and 0 < int(s[i:i+2]) < 27:
                ans+=d2
        d1,d2 = ans,d1

    '''
    dp = [1]*(l+1)
    for i in range(l-1,-1,-1):
        if s[i] == '0':
            dp[i] = 0
            continue
        dp[i] = dp[i+1]
        if i+2 <= l and 0 < int(s[i:i+2]) < 27:
            dp[i]+=dp[i+2]
    
    return dp[0]
    '''
    '''
    @cache
    def dp(i):
        if i >= l:
            return 1
        if s[i] == '0':
            return 0

        ans = dp(i+1)
        if i+2 <= l and 0 < int(s[i:i+2]) < 27:
            ans+=dp(i+2)
        return ans
    return dp(0)
    '''
    return ans


for t in test_case:
    print(func(t))
