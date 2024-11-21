'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''
def isAnagram(s: str, t: str) -> bool:
    if not len(s) == len(t):
        return False
    ss = set(s)
    for i in ss:
        if not s.count(i) == t.count(i):
            return False
    return True

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    ''' anagrams '''
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    print(anagrams)
    return list(anagrams.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
