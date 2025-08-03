'''
2787. Ways to Express an Integer as Sum of Powers
Medium
Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.


'''
from functools import cache
edge_case = [[213,1],[10,2],[11,2],[100,1], [100,100], [100,3], [4,1], [5,1]]

def func(n: int,k: int)->int:
    @cache
    def dp(i,n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        power = i**k
        if n-power < 0 :
            return 0
        return dp(i+1,n-power) + dp(i+1,n)

    return dp(1,n)%(10**9+7)

for n,k in edge_case:
    print(func(n,k))
