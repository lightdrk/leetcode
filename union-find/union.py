class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n
        self.length = n

    def find(self, x):
        #inverse of Ackermann function 
        #O(alpha or inverse (n)) close to constant
        if x >= self.length:
            return -1
        if self.parent[x] != x:
            #find function helps go to source for example
            '''
                if in graph or something we have [2,4]
                and before it is [0,2]
                that meaning for 2 source is 0 and for 4 source is also 0
                and hence we have to move till we dont find source meaning 
                tha value to find is already equal to found.
            '''
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
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

    def __str__(self):
        output = ""
        for i,n in enumerate(self.parent):
            output+=f'{n} <-> {i}\n'
        return output


uf = UnionFind(5)
print(uf)
uf.union(0,2)
print(uf)
uf.union(1,0)
uf.union(1,5)
print(uf)
