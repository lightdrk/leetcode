def Bwb(s, wordDict):
    ln = len(s)
    memo = {}
    def recur(ss):
        if ss == s:
            return True
        if len(ss) > ln:
            return False
        if ss in memo:
            return memo[ss]
        for word in wordDict:
            comb = ss+word
            boolean = recur(ss+word)
            memo[comb] = boolean 
            if recur(comb):
                return True
    for word in wordDict:
        if recur(word):
            return True

    return False

def wb(s, wordDict):
    wordDict = set(word for word in wordDict)
    ln = len(s)

    def recur(start):
        if start >= ln:
            return False
        if s[0:start] in wordDict and s[start:] in wordDict:
            return True
        for i in range(ln):
            if recur(i):
                return True


        return False

    for 






print(wb('leetcode', ["leet", "code"]))
print(wb('applepenapple', ["apple","pen"]))
print(wb('catsandog', ["cats","dog","sand","and","cat"]))

s="bccdbacdbdacddabbaaaadababadad"
wordDict = ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
print(wb(s, wordDict ))



