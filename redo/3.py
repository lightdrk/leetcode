'''
longest substring without repeating characters

Given a string s, find the length of the longest substring without duplicate characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left = 0
        length = 0
        for right in range(len(s)):
            hash_map[s[right]] = hash_map.get(s[right],0) + 1
            while len(hash_map) != (right-left+1):
                hash_map[s[left]]-=1
                if hash_map[s[left]] == 0:
                    hash_map.pop(s[left])
                left+=1
            length = max(length, right-left+1)
        return length


'''

 variation
👉 Problem:
Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

problem statment , say k distinct chars , meaning we can have k unique chars ?

if 
Return the substring itself

Instead of just length, return the actual longest substring.

Keep track of the start index of the current max window.

what if 

Count the number of substrings with at most k distinct characters

Instead of just the longest, count all valid substrings.

Requires a different formula using the current window size.


'''


edge = [["aaaaaabc",2], ["",0], ["aaaaaaaaaaaaaaaaaaa", 10], ["a", 1], ["aabbccdd", 5]]

def func(s,k):
    hash_map = {}
    left = 0
    length = 0
    stringo = ''
    numberOf = 0
    for right in range(len(s)):
        hash_map[s[right]] = hash_map.get(s[right],0) + 1
        while len(hash_map) > k:
            hash_map[s[left]]-=1
            if hash_map[s[left]] == 0:
                hash_map.pop(s[left])
            left+=1
        length = max(length, right-left+1)
        stringo = max(stringo,s[left:right+1],key=len)
        numberOf+=(right-left+1)
    return length, stringo, numberOf


for s,k in edge:
    print(func(s,k))

'''
Streaming / online version

Characters are coming one by one, and you need to maintain the longest valid substring seen so far.

Sliding window + hashmap can still be adapted with a deque or similar.



Dynamic k

k changes per query.

You might precompute or maintain multiple windows.

'''
