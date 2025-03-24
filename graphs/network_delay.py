from collections import deque
def networkDelay(times,n,k):
    matrix = [[0]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)
    for f, t, val in times:
        matrix[f][t] = val
    que = deque([(k,0)])
    time_taken = 0
    while que:
        node, taken = que.popleft()
        print(que)
        if visited[node] == 0:
            visited[node] = 1
        for n, val in enumerate(matrix[node]):
            if val != 0 and visited[n]!=1:
                print(n)
                que.append((n,taken+val))
        time_taken = taken
    return -1 if 0 in visited[1:] else time_taken



#print(networkDelay([[2,1,1],[2,3,1],[3,4,1]],4,2))
#print(networkDelay([[1,2,1]],2,1))
#print(networkDelay([[1,2,1]],2,2))
#print('**************')
#print(networkDelay([[1,2,1],[2,1,3]],2,2))
print(networkDelay([[1,2,1],[2,3,2],[1,3,2]],3,1))
