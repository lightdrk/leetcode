def valid(edges,n):
    graph = {}
    for i,j in edges:
        if not i in graph:
            graph[i] = []
        if not j in graph:
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)

    visited = set()
    stack = [0]
    while stack:
        node = stack.pop()
        if not node in visited:
            visited.add(node)
        else:
            return False
        for i in graph[node]:
            if not i in visited:
                stack.append(i)
    return True

print(valid([[0, 1], [0, 2], [0, 3], [1, 4]],5))
print(valid([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],5))
print(valid([[0, 1], [1, 2], [1, 3], [1, 4], [4, 5], [4, 6], [6,7], [7, 5]],8))

