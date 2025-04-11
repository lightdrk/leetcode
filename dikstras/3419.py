import heapq
from collections import defaultdict, deque


def TminMaxWeight(n, edges, threshold):

    adj_list = defaultdict(list)
    for fr, to, weight in edges:
        adj_list[fr].append([to, weight])

    mn = -1
    for nn in range(1,n):
        pq = [(0,nn)]
        distance = [float('inf')]*n
        while pq:
            weight, source = heapq.heappop(pq)
            for node, w in adj_list[source]:
                new_dist = weight+w
                if distance[node] > new_dist:
                    distance[node] = new_dist
                    heapq.heappush(pq,(new_dist,node))
        if distance[0] == float('inf'):
            return -1
        print(f'from {nn} -> 0 , distance: {distance}')
        if mn < min(distance):
            mn = min(distance)

    return mn


def minMaxWeight(n, edges, threshold):
    def isPossible(bound):
        adj_list = defaultdict(list)
    
        for fr, to, we in edges:
            if we <= bound:
                adj_list[to].append([fr,we])

        visited = [False]*n
        visited[0] = True
        que = deque([0])
        while que:
            node = que.popleft()
            for s, weight in adj_list[node]:
                if not visited[s]:
                    visited[s] = True
                    que.append(s)
        for i in range(1,n):
            if not visited[i]:
                return False

        return True
    ans = -1
    left = 0
    right = max(w for _,_,w in edges)
    while left<=right:
        mid = (right+left)//2
        if isPossible(mid):
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans
        

print(minMaxWeight(5, [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], 2))
print(minMaxWeight(5, [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]], 1))
print(minMaxWeight(5, [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]], 1))
print(minMaxWeight(4, [[3,2,24],[3,0,92],[2,1,8],[3,2,87],[1,3,20]], 3))

