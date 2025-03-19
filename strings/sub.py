def subString(s):
    hash_map = {}
    mx = 0
    l = 0
    for i,char in enumerate(s):
        if char in hash_map:
            if mx < hash_map[char] - i:
            hash_map[char] = i
            hash_map[char] = i
        else:

