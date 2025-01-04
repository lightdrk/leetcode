def canFinish(n,pre):
    graph = {i: [] for i in range(n)}
    for i,j in pre:
        graph[j].append(i)

    visited = [0] * n
    for node in range(n):
        if visited[node] == 0:
            stack = [node]
            while stack:
                node = stack.pop()
                visited[node] = 1
                for i in graph[node]:
                    if visited[i] == 1:
                        return False
                    if visited[i] == 0:
                        stack.append(i)
                visited[node] = 2
                print(visited)

    return True
canFinish(5,[[1,4],[2,4],[3,1],[3,2]])
canFinish(2,[[1,0],[0,1]])
