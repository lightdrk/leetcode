import heapq
from collections import defaultdict


def prims(n, edges):
    graph = defaultdict(list)

    for u,v,w in edges:
        graph[u].append((w,v))
        graph[v].append((w,u))


    visited = set()
    pq = [(0,0)]
    total_cost = 0
    
    while len(visited) < n:
        weight, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(weight)
        total_cost+=weight
        visited.add(node)
        for nw, ni in graph[node]:
            if not ni in visited:
                heapq.heappush(pq, (nw, ni))
    return total_cost

# (u, v, weight)
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
]

n = 6  # number of nodes (0 to 5)

print(prims(n,edges))
