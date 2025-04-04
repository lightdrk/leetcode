import time
import heapq



def dikStras(matrix):
    pq = heapq.heapify([(0,0)])
    visited = [False]*len(matrix)
    distance = [float('inf')]*len(matrix)
    while pq:
        distance, node = heapq.heappop(pq)
        if not visited[node]:
            visited[node] = True
        for i,n in enumerate(matrix[node]):
            if not visited[i]:

start = time.time()



