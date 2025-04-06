import heapq
from collections import defaultdict


def findCheapestPrice( n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int|float:
        #can not go stop > k
        adj_list = defaultdict(list)
        for f,t,p in flights:
            adj_list[f].append((p,t))

        distance = [float('inf')]*n
        pq = [(0,src,0)]
        while pq:
            dist,node,hop = heapq.heappop(pq)
            if hop > k:
                continue
            for p,t in adj_list[node]:
                new_dist = dist+p
                if distance[t] > new_dist:
                    distance[t]=new_dist
                    heapq.heappush(pq,(new_dist,t,hop+1))
        print(distance)
        return distance[dst]     



#print(findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))

print(findCheapestPrice(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))
#print(findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))
#print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
#print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
#print(findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))
print(findCheapestPrice(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))
#778. Swim in Rising Water
#815. Bus Routes
#1091. Shortest Path in Binary Matrix
#1631. Path With Minimum Effort
#2812. Find the Safest Path in a Grid
#2642. Design Graph With Shortest Path Calculator
