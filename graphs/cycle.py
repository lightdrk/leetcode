def isCycle(matrix):
    graph = {}
    for i,j in matrix:
        if not i in graph:
            graph[i] = []
        if not j in graph:
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)
    visited = set()
    stack = [(0, None)]
    while stack:
        node, parent = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for i in graph[node]:
            if not i in visited:
                stack.append((i,node))
            elif i != parent:
                return True
    return False

def isCycleDirected(matrix):
    graph = {}
    for i,j in matrix:
        if not i in graph:
            graph[i] = []
        grpah[i].append(j)

    visited = set()
    stack = [(0,None)]
    while stack:
        node,parent = stack.pop()
        if node in visited:
            continue


print(isCycle([[0,1],[1,2],[2,3],[3,1]]))

