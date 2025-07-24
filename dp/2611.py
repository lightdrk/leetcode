'''
There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.

A point of the cheese with index i (0-indexed) is:

reward1[i] if the first mouse eats it.
reward2[i] if the second mouse eats it.
You are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.

Return the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.
'''
#lets try if it is possible using dp
from functools import cache

def mice(r1,r2,k):
    l = len(r1)
    @cache
    def dp(i,k)->int:
        if i >= l:
            return 0
        if k == 0:
            return sum(r2[i:])
        return max(r1[i]+dp(i+1,k-1), r2[i]+dp(i+1,k))
    return dp(0,k)

print(mice([3,1,1,3],[3,2,3,1],3))
