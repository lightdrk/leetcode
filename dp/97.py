def iisInterleave(s1,s2,s3):
    length1 = len(s1)
    length2 = len(s2)
    def recur(i,j, word):
        if i == length1 and j == length2:
            return word == s3
        ans = False
        if i < length1:
            ans = ans or recur(i+1,j, word+s1[i])
        if j < length2:
            ans = ans or recur(i,j+1, word+s2[j])
        return ans
    return recur(0,0,'')

#print(isInterleave('aabcc','dbbca','aadbbcbcac'))
#print(isInterleave('aabcc','dbbca','aadbbbaccc'))



'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
'''


'''
question was easy except i was using comparision , with word and also building the word which was wrong
as it was increase the time

'''


##trick was to not create a string , rather check if s3[i+j] == s1[i] , s2[j]..


def isInterleave(s1,s2,s3):
    length1 = len(s1)
    length2 = len(s2)
    if length1 + length2 != len(s3):
        return False
    memo = {}
    def recur(i,j):
        if i == length1 and j == length2:
            return True
        if (i,j) in memo:
            return memo[(i,j)]
        ans = False
        if i < length1 and s1[i] == s3[i+j]:
            ans = ans or recur(i+1,j)
        if j < length2 and s2[j] == s3[i+j]:
            ans = ans or recur(i,j+1)
        memo[(i,j)] = ans
        return ans
    return recur(0,0)

print(isInterleave('aabcc','dbbca','aadbbcbcac'))
print(isInterleave('aabcc','dbbca','aadbbbaccc'))


