def requests(n: int, requests: list):
    parents = [i for i in range(n)]
    rank = [0]*(n)
    counter = n
    def find(m: int):
        if m != parents[m]:
            parents[m] = find(parents[m])

        return parents[m]

    def union(i,j):
        nonlocal counter
        rootX = find(i)
        rootY = find(j)
        if rootX == rootY:
            return
        counter -=1
        if rank[rootX] > rank[rootY]:
            parents[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parents[rootX] = rootY
        else:
            parents[rootY] = rootX
            rank[rootX]+=1
    
    ans: list[int] = []
    for n1,n2 in requests:
        union(n1,n2)
        print(parents)
        ans.append(counter)
    return ans

print(requests(5, [(0, 1), (2, 3), (1, 2), (0, 4)]))

