'''
1653. Minimum Deletions to Make String Balanced
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

'''
'''
1. so the answer is independent of how many a and b's we are looking for a way where 'a' starts and ends then b stars and end 
2. i will never should exceed the length
3. order matters if we have a and b in string ,then a will alwys be first 
question : if we only have a will that count as balanced ?
answer -> if we only have a's that too is considered balanced

'''
from collections import Counter

def minD(s: str)->int:
    i = 0
    l = len(s)
    # bellow will remove starting b's
    while i < l and s[i] != 'a':
        i+=1
    if i == l-1:
        return 0
    count_map = Counter(s)
    if count_map['a'] < count_map['b'] and (i + 1) >= count_map['a']:
        return count_map['a']

    def remove(i):
        if i >= l:
            return 0
        if count_map[s[i]] == 

        return min(remove(i+1),1+remove(i+1))


    return
