#build the lcs

def build(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    def dp(i,j):
        if i >= l1 or j >= l2:
            return ''

        if str1[i] == str2[j]:
            return str1[i] + dp(i+1,j+1)

        return max(dp(i+1,j), dp(i,j+1), key=len)
    
    return dp(0,0)


print(build("abac", "cab"))
print(build("abcde", "ace"))
