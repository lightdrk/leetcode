def wb(s, wordDict):
    words = set()
    length = 0
    for word in wordDict:
        words.add(word)
        length+=1
    length = len(s)
    def recur(i):
        if s[:idx] in words and s[idx:] in words:
            return True
        for idx in range(i,length):
            if s[:idx] in words:
                recur(idx+1)

