class Uf:
    def __init__(self,n):
        self.length = n
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, x):
        if x >= self.length:
            return -1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        if x >= self.length or y >= self.length:
            return 

        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        else:
            self.rank[rootX]+=1
            self.parent[rootY] = rootX
        return


test = Uf(11)
edges = [[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]
for i,h in edges:
    test.union(i,h)

print(test.parent)



# Union-Find (Disjoint Set Union) with path compression
class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

# Input pairs
edges = [[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]

# Initialize union-find
uf = UnionFind()

# Perform unions
for x, y in edges:
    uf.union(x, y)

# Find root of each node
all_nodes = set(x for pair in edges for x in pair)
final_roots = {node: uf.find(node) for node in all_nodes}

# Output final root mapping
print("Final root of each node:")
for node, root in sorted(final_roots.items()):
    print(f"{node}: {root}")

print(uf.parent)
