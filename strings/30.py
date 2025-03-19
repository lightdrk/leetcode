def findSubstring( s: str, words: list[str]) -> list[int]:
    size = len(words[0])
    window = len(words)*size
    h_window = {}
    for word in words:
        if not word in h_window:
            h_window[word] = 0
        h_window[word]+=1
    length_s = len(s)
    if length_s < window:
        return []
    output = []
    for idx in range(length_s-window+1):
        new_word = s[idx: idx+window]
        print(new_word)
        new_window = {}
        for i in range(0,window,size):
            word = new_word[i:i+size]
            if not word in new_window:
                new_window[word] = 0
            new_window[word]+=1
        if new_window == h_window:
            output.append(idx)
    return output


print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
