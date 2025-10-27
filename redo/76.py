'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
    '''
from collections import Counter

def minWindow(s,t):
    h_t = Counter(t)
    s_t = {}
    left = 0
    output = s+' '
    for right in range(len(s)):
        s_t[s[right]] = s_t.get(s[right],0) + 1
        while (s[left] not in h_t or s_t[s[left]] > h_t[s[left]]) and left < right:
            s_t[s[left]]-=1
            if s_t[s[left]] == 0:
                s_t.pop(s[left])
            left+=1

        if all( (k in s_t and s_t[k] >= h_t[k]) for k in h_t):
            output = min(s[left:right+1],output,key=len)

    return '' if output == s+' ' else output


edge = [['',''], ['abc',''], ['','avd'], ["ADOBECODEBANC", 'ABC'], ['AAAAAAA', 'B'], ['AAAAA', 'A'], ['abcABC', 'aA']]
c=0
for s,t in edge:
    print(f'{c}-> ',minWindow(s,t))
    c+=1


