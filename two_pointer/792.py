'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

'''
def match(s,words):
    count = 0
    l = len(s)
    for word in words:
        idx = 0
        is_sub = True
        for char in word:
            if idx >= l:
                is_sub = False
                break
            for i in range(idx, l):
                if s[i] == char:
                    idx = i+1
                    break
        if is_sub:
            count+=1
    return count

test = [['abc',['a','b','c', 'ac','cb']], ['',['','']], ['aefg', ['afg','ef', 'eg', 'ge']]]
for s,words in test:
    print(match(s,words))


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def search(target,arr,l):
            left= 0
            right = l -1
            ans = -1
            while left<=right:
                mid = left + (right-left)//2
                if arr[mid] >= target:
                    ans = arr[mid]
                    right = mid-1
                else:
                    left = mid+1
            return ans

        count = 0

        hash_map = {}
        for i,char in enumerate(s):
            if not char in hash_map:
                hash_map[char] = [0,[]]
            hash_map[char][1].append(i)
            hash_map[char][0]+=1

        

        for word in words:
            idx = 0
            is_sub = True
            for char in word:
                if (not char in hash_map):
                    is_sub = False
                    break
                found = False
                l,arr = hash_map[char]
                val = search(idx,arr,l)
                if  val != -1:
                    idx = val + 1
                    found = True

                if not found:
                    is_sub = False

            if is_sub:
                count+=1
        return count

        
