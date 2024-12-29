def mostProfitable(edges, bob, amount):
    adj_list = {}
    profit = []
    for k,v in edges:
        if not k in adj_list:
            adj_list[k] = []
        if not v in adj_list:
            adj_list[v] = []
        adj_list[k].append(v)
        adj_list[v].append(k)

    def dfs(start):
        stack = [(start,None, [])]
        visited = [False] * (len(edges) + 1)
        output = []
        while stack:
            node, parent, path = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            curr_path=path + [node]
            if len(adj_list[node]) == 1 and adj_list[node][0] == parent:
                if 0 in curr_path:
                    output.append(curr_path)
            for i in adj_list[node]:
                if not visited[i] and parent != i:
                    stack.append((i,node,curr_path))
        return output

    paths = dfs(0)
    bobs_path = dfs(bob)
    print(paths)
    print(bobs_path)
    profit = []
    for p in paths:
        for b in paths:
            total = 0
            i = 0
            while i < len(p):
                if p[i] == b[i]:
                    total+= amount[p]/2




    #bob will decrese ..
    #those decresed will not add value
    #if intercepted half it 
    #if crossed add value



mostProfitable([[0,1],[1,2],[1,3],[3,4]],3,[-2,4,2,-4,6])

