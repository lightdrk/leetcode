!not complete

def redundant(edges :list[list[int]]) -> list[int]:
    graph = {}
    for i,j in edges:
        if not i in graph:
            graph[i] = []
        if not j in graph:
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)

    output = []
    visited = set()
    stack = []
    stack.append(1)
    while stack:
        x = stack.pop()
        if not x in visited:
            visited.add(x)
        for i in graph[x]:
            if i in visited:
                output.append([x,i])
            else:
                stack.append(i)
    return output

print(redundant([[1,2],[1,3],[2,3]]))

print(redundant([[1,2],[2,3],[3,4],[1,4],[1,5]]))
