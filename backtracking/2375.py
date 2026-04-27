"""
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

"""

test_case = [["IIIDIDDD", "123549876"],["DDD","4321"]]
def smallestNumber(pattern: str)-> str:
    l = len(pattern)
    ans = [987654321]

    def bk(i: int,s: int):
        if i >= l:
            ans[0] = min(s,ans[0])
            return
        n = s%10
        if pattern[i] == "I":
            for x in range(n+1,10):
                if used[x-1]:
                    continue
                used[x-1] = True
                bk(i+1,(s*10)+x)
                used[x-1] = False
        else:
            for x in range(n-1,0,-1):
                if used[x-1]:
                    continue
                used[x-1] = True
                bk(i+1,(s*10)+x)
                used[x-1] = False
    for i in range(1,10):
        used = [False]*(9)
        used[i-1] = True
        bk(0,i)
    return str(ans[0])

for t,a in test_case:
    print(smallestNumber(t)==a)




