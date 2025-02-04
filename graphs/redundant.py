def redun(edges):
    length = len(edges)
    graph = {i: [] for i in range(1,length+1)}
    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
    visited = [0]*(length+1)

    st = [1]
    output = []
    while st:
        node = st.pop()
        if visited[node] == 1:
            continue
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 1:
                output.append([node,i])
            else:
                st.append(i)
    print(output)

redun([[1,2],[1,3],[2,3]])

redun([[1,2],[2,3],[3,4],[1,4],[1,5]])



