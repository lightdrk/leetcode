'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.


'''

def func(edge):
    l = len(edge)
    visited = [False]*l
    mx_cycle = -1
    for i in range(l):
        if edge[i] == -1:
            continue
        stack = [(i, dict())]
        cycle = 0
        while stack:
            idx, hash_map = stack.pop()
            if (idx in hash_map):
                cycle-=(hash_map[idx] - 1)
                continue
            if visited[idx] or edge[idx] == -1:
                cycle = -1
                break
            cycle+=1
            visited[idx] = True
            hash_map[idx] = cycle
            stack.append((edge[idx],hash_map))
        if mx_cycle < cycle:
            mx_cycle = cycle

    return mx_cycle

case = [[3,3,4,2,3], [1,2,3,3], [1,0],[-1,0], [-1,-1,-1], [0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,5],[2,2,3,1],[1,0,3,2,5,6,4]]

for t in case:
    print(func(t))
