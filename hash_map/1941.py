from collections import Counter

def occur(s):
    return len(set(Counter(s).values())) == 1
print(occur("abacbc"))
