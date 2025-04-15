class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.length = n

    def find(self, x):
        if x >= self.length:
            return -1

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        if x >= self.length:
            return 
        if y >= self.length:
            return

        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX]+=1

def kruskal(edges):
    edges = sorted(edges, key=lambda x: x[2])
    d = DSU(len(edges))
    mst = []
    for u,v,w in edges:
        if d.find(u) != d.find(v):
            mst.append([u,v,w])
            d.union(u,v)
    return mst

print(kruskal([(0,1,1),(0,2,3),(1,2,2),(2,4,4),(2,4,5)]))
