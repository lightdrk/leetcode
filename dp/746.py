import sys

sys.setrecursionlimit(10000)

def minCost(cost, idx):
    if idx >= len(cost):
        return 0
    m1 = minCost(cost,idx+1)
    m2 = minCost(cost, idx+2)
    if m1 < m2:
        return cost[idx]+m1
    return cost[idx]+m2


print(min(minCost(cost,0), minCost(cost,1)))
