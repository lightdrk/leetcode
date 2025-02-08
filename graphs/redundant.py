def redun(edges):
    length = len(edges)
    graph = {i: [] for i in range(1,length+1)}
    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
    visited = [False]*(length+1)
    st = [(1,None)]
    output = []
    while st:
        node,parent = st.pop()
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                st.append((i,node))
            if parent != i:
                output.append([i,parent])

    print(output)

redun([[1,2],[1,3],[2,3]])

redun([[1,2],[2,3],[3,4],[1,4],[1,5]])



