"""
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
"""
test_case = [[1,3],[1,4],[3,9]]

def getHappyString(n,k):
    arr = []
    total = [0]
    constant = "abc"
    def bk(i:int,a:str):
        if i == n:
            total[0]+=1
            arr.append(a)
            return
        for c in constant:
            if a and a[-1] == c:
                continue
            bk(i+1,a+c)
    bk(0,'')
    return arr[k-1] if k<= total[0] else ''


for n,k in test_case:
    print(getHappyString(n,k))
