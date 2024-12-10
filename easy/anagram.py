def a(s,t):
    if not len(s) == len(t):
        return False
    freq = {}
    for char_s, char_t in zip(s,t):
        if char_s in freq:
            freq[char_s] = freq[char_s] + 1
        else:
            freq[char_s] = 1
        if char_t in freq:
            freq[char_t] = freq[char_s] - 1
        else:
            freq[char_t] = -1
        print(freq)
    print(freq)
    return all(v == 0 for v in freq.values())

print(a('anagram','nagaram'))
