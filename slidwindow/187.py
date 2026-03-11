test_case = ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT","AAAAAACCCCCTTTAAAAAACCCCCCAAAAAGGGTTT"]

def dna(s):
    l = len(s)
    hash_map = {}
    window = s[:10]
    hash_map[window] = 1
    for i in range(10,l):
        hash_map[window] = hash_map.get(window,0)+1
        window = window[1:]+s[i]

    print(hash_map)
    return [key for key in hash_map if hash_map[key]>1]


for t in test_case:
    print(dna(t))
