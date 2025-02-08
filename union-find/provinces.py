class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x :int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX]+=1
    def __str__(self):
        return f'{self.parent}'

def pro(n :int, matrix :list[list[int]]):
    uf = UnionFind(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                uf.union(i,j)
    print(uf)
    count = 0
    for i in range(n):
      if uf.find(i) == i:
        count+=1
    return count


n = 4
matrix = [
  [1, 1, 0, 0],
  [1, 1, 0, 0],
  [0, 0, 1, 1],
  [0, 0, 1, 1]
]

print(pro(n,matrix))
n = 5
matrix = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 0, 0, 1]
]

print(pro(n,matrix))

n = 8
isConnected = [
  [1, 0, 0, 1, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 1]
]

print(pro(n,matrix=isConnected))
