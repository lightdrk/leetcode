'''
the only thing i was doing wrong was recur(i+2,j+1)
which was wrong , to skip the choice i should be doing recur(i+1, j)
this was what i checked on chat gpt 
'''


def numDistinct(s, t):
    length = len(s)
    lengtht = len(t)
    if length < lengtht:
        return 0
    memo = {}
    def recur(i,j):
        if j == lengtht:
            return 1
        if i == length and j < lengtht:
            memo[(i,j)] = 0
            return 0
        if s[i] == t[j]:
            memo[(i,j)] = recur(i+1,j+1) + recur(i+1, j)
        else:
            memo[(i,j)] = return recur(i+1,j)

        return memo[(i,j)]
    return recur(0,0)

print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("babgbag", "bag"))


