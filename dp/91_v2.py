'''
def num(s: str) -> int:
    decoded = set(str(i) for i in range(1,27))
    length = len(s)
    cache = {}
    def recur(i):
        if i >= length:
            return 1
        if s[i] == '0':
            return 0
        if i in cache:
            return cache[i]
        ans = 0
        if s[i] in decoded:
            ans+=recur(i+1)
        if i+1<length and s[i:i+2] in decoded:
            ans+=recur(i+2)
        cache[i] = ans
        return ans
    return recur(0)


print(num('12121'))
'''

def num(s :str) ->int:
    length = len(s)
    dp = [0]*(length+1)
    dp[length] = 1
    for i in range(length-1,-1,-1):
        if s[i] != '0':
            dp[i]+=dp[i+1]

        if '10' <= s[i:i+2] <= '26' and i+1 < length:
            dp[i]+=dp[i+2]

    return dp[0]

print(num('12121'))
