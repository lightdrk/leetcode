'''
You are given an integer n.

In one operation, you may split an integer x into two positive integers a and b such that a + b = x.

The cost of this operation is a * b.

Return an integer denoting the minimum total cost required to split the integer n into n ones.

'''

test_case = [10,1,3,5,7,9,11,13,52,59,60,69,65,68,70,77,75,100,105,120,131,19,500,496]

class Solution:
    hash_map :list[int] = [-1]*501
    hash_map[0]= 0
    hash_map[1] = 0
    def minCost(self,n: int) ->int:
        if self.hash_map[n] > -1:
            return self.hash_map[n]
        half = n//2
        self.hash_map[n] = half*(n-half)+self.minCost(half)+self.minCost(n-half)
        return self.hash_map[n]

sol = Solution()
for t in test_case:
    print(t,'-->',sol.minCost(t))
