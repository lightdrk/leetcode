'''
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

'''

test_case = [[6,[[0,1],[0,2],[2,5],[3,4],[4,2]]],[5,[[0,1],[2,1],[3,1],[1,4],[2,4]]], [3,[[1,2],[1,0],[0,2]]]]

def find(n,edges)-> list[int]:
    '''fails in third case as we are only looking for linearly and their 
    could be a solution where later node can visite all of the nodes
    so it fails in that case'''

    ans = []
    visited = set()
    hash_map = {i:[] for i in range(n)}
    for f,t in edges:
        hash_map[f].append(t)

    for i in range(n):
        if i in visited:
            continue
        stack = [i]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for j in hash_map[node]:
                if j in visited:
                    continue
                stack.append(j)
        ans.append(i)

    return ans


for n,e in test_case:
    print(find(n,e))
