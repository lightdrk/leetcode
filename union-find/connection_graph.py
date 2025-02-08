class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n
        self.length = n

    def find(self,x):
        #return root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x]+=1

def graph(n,edges):
    uf = UnionFind(n)
    for i,j in edges:
        uf.union(i,j)

    components = {}
    for i in range(n):
        root = uf.find(i)
        if not root in components:
            components[root] = []
        components[root].append(i)
    return list(components.values())

print(graph(6,[(0,1),(1,2),(3,4),(4,5)]))


def graph_(n,edges):
    graph = {i:[] for i in range(n)}
    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
    visited = set()
    output = []
    def dfs(i,connected):
        visited.add(i)
        connected.append(i)
        for node in graph[i]:
            if not node in visited:
                dfs(node,connected)
        return connected

    for i in range(n):
        if not i in visited:
            output.append(dfs(i,[]))
    return output

print(graph_(6,[(0,1),(1,2),(3,4),(4,5)]))



