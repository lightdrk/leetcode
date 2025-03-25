import heapq

def networkDelay(times,n,k):
    matrix = [[float('inf')]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)
    for f, t, val in times:
        matrix[f][t] = val
    print(matrix)
    que = [(0,k)]
    distance = [float('inf')]*(n+1)
    distance[k] = 0
    while que:
        taken, node = heapq.heappop(que)
        if visited[node]:
            continue
        visited[node] = 1
        for n, val in enumerate(matrix[node]):
            if val != float('inf') and visited[n] == 0:
                new = taken+val
                if distance[n] > new:
                    distance[n] = new
                    heapq.heappush(que,(new,n))
    print(distance)
    #return -1 if 0 in visited[1:] else time_taken



print(networkDelay([[2,1,1],[2,3,1],[3,4,1]],4,2))
#print(networkDelay([[1,2,1]],2,1))
#print(networkDelay([[1,2,1]],2,2))
#print('**************')
#print(networkDelay([[1,2,1],[2,1,3]],2,2))

print(networkDelay([[1,2,1],[2,3,2],[1,3,2]],3,1))

test = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
networkDelay(test,5,5)
