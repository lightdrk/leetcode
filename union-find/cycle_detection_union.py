class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n

    def find(self,x):
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
            self.parent[x] = y
            self.rank[x]+=1

def isCyclic(n :int, edges :list[tuple])->bool:
    uf = UnionFind(n)
    for i,j in edges:
        if uf.find(i) == uf.find(j):
            return True
        else:
            uf.union(i,j)
    return False


test_cases = [
    (4, [(0, 1), (1, 2), (2, 3), (3, 0)],True),  # Cycle detected
    (5, [(0, 1), (2, 3)],False),  # No cycle, 3 components
    (3, [(0, 1), (1, 2)], False),  # No cycle, 1 component
    (5, [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4)], True),  # Cycle detected
    (6, [(0, 1), (2, 3)], False),  # No cycle, 4 components
]
for n,edges,output in test_cases:
    print(isCyclic(n,edges) == output)
