import time
import heapq



def dikStras(matrix):
    pq = [(0,0)]
    distance = [float('inf')]*len(matrix)
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
            continue
        
        for i,n in enumerate(matrix[node]):
            if n == -1 or n == float('inf'):
                continue
            new_dist = dist+n
            if new_dist < distance[i]:
                distance[i] = new_dist
                heapq.heappush(pq,(new_dist, i))
    return distance

matrix = [
    [0,10,-1,30],
    [10,0,50,10],
    [-1,50,0,20],
    [30,10,20,0]
] 

adj_matrix_1 = [
    [0, 1, 4, float('inf')],  # Node 0 connections
    [1, 0, 2, 5],             # Node 1 connections
    [4, 2, 0, 1],             # Node 2 connections
    [float('inf'), 5, 1, 0]   # Node 3 connections
]

adj_matrix_2 = [
    [0, 2, 4, float('inf'), float('inf')],  # Node 0 connections
    [2, 0, 1, 7, float('inf')],             # Node 1 connections
    [4, 1, 0, 3, 5],                        # Node 2 connections
    [float('inf'), 7, 3, 0, 1],             # Node 3 connections
    [float('inf'), float('inf'), 5, 1, 0]   # Node 4 connections
]

adj_matrix_3 = [
    [0, 3, float('inf'), float('inf')],  # Node 0 connections
    [3, 0, 2, float('inf')],             # Node 1 connections
    [float('inf'), 2, 0, 1],             # Node 2 connections
    [float('inf'), float('inf'), 1, 0]   # Node 3 connections
]
start = time.time()
print(dikStras(matrix))
print(dikStras(adj_matrix_1))
print(dikStras(adj_matrix_2))
print(dikStras(adj_matrix_3))

end=time.time()

print(end-start)


