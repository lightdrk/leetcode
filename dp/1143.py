def longestCS(text1, text2):
    #text1 generate subsequences
    #text2 generate sub
    length1 = len(text1)
    length2 = len(text2)
    output1 = set()
    output2 = []
    def recur1(word,i):
        if i == length1:
            output1.add(word)
            return
        recur1(word+text1[i], i+1)
        recur1(word, i+1)

    def recur(word,i):
        output2.append(word)
        for idx in range(i,length2):
            recur(word+text2[idx],idx+1)
    recur1('',0)
    recur('',0)
    ans = 0
    for word in output2:
        if word in output1:
            ans = max(ans, len(word))

    return ans

print(longestCS("abcde", "ace"))

