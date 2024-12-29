def mostProfitable(edges, bob, amount):
    print(len(edges))
    adj_list = {}
    profit = []
    for k,v in edges:
        if not k in adj_list:
            adj_list[k] = []
        if not v in adj_list:
            adj_list[v] = []
        adj_list[k].append(v)
        adj_list[v].append(k)
    start = 0
    stack = [(start,None, [])]
    visited = [False] * (len(edges) + 1)
    while stack:
        node, parent, path = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        curr_path=path + [node]
        if len(adj_list[node]) == 1 and adj_list[node][0] == parent:
            print(curr_path)
            if bob in curr_path:
                s = bob
                su = 0
                for n in curr_path:
                    su = n
                    if n == s:
                        su+=amount[n]/2
                    elif n>s:
                        su
                    else:


        for i in adj_list[node]:
            if not visited[i] and parent != i:
                stack.append((i,node,curr_path))

mostProfitable([[0,1],[1,2],[1,3],[3,4]],3,[-2,4,2,-4,6])

