import heapq

def dikstras(matrix,start):
    length = len(matrix)
    visited = [0]*length
    distance = [float('inf')]*length
    que = [(0,start)]

    while que:
        dist, curr = heapq.heappop(que)
        if visited[curr]:
            continue
        visited[curr] = 1
        for node, weight in enumerate(matrix[curr]):
            if weight > 0 and visited[node] == 0:
                dist+=weight
                if distance[node] > dist:
                    distance[node] = dist
                    heapq.heappush(que, (dist, node))
    return distance


graph = [
    [0, 1, 0, 4, 0],  # A
    [1, 0, 3, 1, 0],  # B
    [0, 3, 0, 0, 1],  # C
    [4, 1, 0, 0, 2],  # D
    [0, 0, 1, 2, 0],  # E
]

start = 0

print(dikstras(graph, start))
