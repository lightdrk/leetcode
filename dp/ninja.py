from functools import cache
import random

def ninja(n, points):
    @cache
    def dp(i,j):
        if i == n:
            return 0
        ans = 0
        for y in range(3):
            if y == j:
                continue
            ans = max(ans, points[i][y]+dp(i+1,y))
        return ans

    return dp(0,-1)

print(ninja(3, [[1,2,5], [3 ,1 ,1] ,[3,3,3]]))
print(ninja(3, [[10,40, 70], [20 ,50 ,80] ,[30,60,90]]))


N = 10**2  # 100,000 days
activities = 3

# Generate the test case
points = [[random.randint(1, 100) for _ in range(activities)] for _ in range(N)]

print(ninja(N, points))
