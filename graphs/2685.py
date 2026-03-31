'''
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

'''
test_case = [[6,[[0,1],[0,2],[1,2],[3,4]]], [6,[[0,1],[0,2],[1,2],[3,4],[3,5]]]]


def countCompleteComponents(n, edges)->int:
    '''
    connected are those which are completely connected meaning edges between all shoud have all
    '''
    count = 0
    hash_map = {i: [] for i in range(n)}
    for f,t in edges:
        hash_map[f].append(t)
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        stack = [i]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for d in hash_map[node]:
                if d in visited:
                    continue
                stack.append(d)
        count+=1

    return count 

def countCompleteComponents(n,edges):
    count = 0
    hash_map = {i: [] for i in range(n)}
    for f,t in edges:
        hash_map[f].append(t)
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        stack = [i]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for d in hash_map[node]:
                if d in visited:
                    continue
                stack.append(d)
        count+=1

    return count 






for n,t in test_case:
    print(countCompleteComponents(n,t))

