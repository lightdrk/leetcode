'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


'''

import heapq

test_case = [[[0,0],[2,2],[3,10],[5,2],[7,0]],[[3,12],[-2,5],[-4,1]]]

def minCost(points):
    l = len(points)
    visited = [False]*l
    heap = [(0,0)]
    goal = 0
    path = []
    while heap:
        ans,idx = heapq.heappop(heap)
        if visited[idx]:
            continue
        goal+=ans
        path.append(points[idx])
        for i in range(l):
            if visited[i]:
                continue
            heapq.heappush(heap,(abs(points[i][0]-points[idx][0])+abs(points[i][1]-points[idx][1]),i))
        visited[idx] = True
    print(path)
    return goal


for t in test_case:
    print(minCost(t))
