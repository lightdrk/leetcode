def permutaition(s1, s2):
    s1_length = 0
    s1_counter = {}
    for char in s1:
        if not char in s1_counter:
            s1_counter[char] = 0
        s1_counter[char]+=1
        s1_length+=1

    s2_counter = Counter(s2[:s1_length])

