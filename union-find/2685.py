'''
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.


'''
def func(n, edges):
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    def union(x,y):
        rootX = find(x)
        rootY = find(y)

        if rootX < rootY:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY

    adj_list = {i: [] for i in range(n)}
    for i,j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)
        union(i,j)
    print(adj_list)
    print(parent)
    no = set()
    for i in range(n):
        if parent[i] in no:
            no.add(i)
            continue
        if parent[i] != i and not n in adj_list[parent[i]]:
            no.add(i)
    print(no)
    return 

test = [[6, [[0,1],[0,2],[1,2],[3,4]]],[6, [[0,1],[0,2],[1,2],[2,3],[3,4]]], [6, [[0,1],[0,2],[2,3],[3,4]]]]


for n,edges in test:
    func(n,edges)
