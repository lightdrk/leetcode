def conn_comp(n :int, edges: list[list[int]]) ->int:
    def dfs(i):
        stack =[i]
        while stack:
            i = stack.pop()
            if not i in visited:
                visited.add(i)
            for x in graph[i]:
                if x not in visited:
                    stack.append(x)

    graph = {n:[] for n in range(n)}
    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)

    visited = set()
    comps = 0
    for key in graph:
        if not key in visited:
            comps+=1
            dfs(key)
    return comps

print(conn_comp(3,[[0,1]]))



test_cases = [
    [7, [[0, 1], [1, 2], [3, 4], [5, 6]], 3],  # 3 connected components: [0-1-2], [3-4], [5-6]
    [10, [[0, 1], [1, 2], [3, 4], [5, 6], [7, 8]], 5],  # 5 connected components: [0-1-2], [3-4], [5-6], [7-8], [9]
    [8, [[0, 1], [1, 2], [2, 3], [4, 5], [6, 7]], 3],  # 4 connected components: [0-1-2-3], [4-5], [6-7], [8]
    [5, [[0, 1], [1, 2], [2, 3], [4, 0]], 1],  # 1 connected component: [0-1-2-3-4]
    [6, [[0, 1], [2, 3], [4, 5], [0, 2], [1, 4]], 1],  # 1 connected component: [0-1-2-3-4-5]
    [6, [[0, 1], [1, 2], [3, 4], [4, 5]], 2],  # 2 connected components: [0-1-2], [3-4-5]
    [9, [[0, 1], [2, 3], [4, 5], [6, 7], [8, 0]], 4],  # 3 connected components: [0-1-8], [2-3], [4-5], [6-7]
    [7, [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6]], 2],  # 2 connected components: [0-1-2-3], [4-5-6]
]

for n,i,x in test_cases:
    print(conn_comp(n,i) == x)

test_cases = [
    [101, [[i, i+1] for i in range(100)], 1],  # 1 connected component: [0-1-2-...-100]
    [150, [[i, i+1] for i in range(149)] + [[i, i+2] for i in range(148)], 1],  # 1 connected component with chains and extra edges
    [200, [[i, i+1] for i in range(199)] + [[100, 150]], 2],  # 2 connected components: [0-1-2-...-99] and [100-150-...-199]
    [250, [[i, i+1] for i in range(249)] + [[50, 100], [150, 200]], 2],  # 2 connected components: [0-1-2-...-49] and [50-100-...-249]
    [300, [[i, i+1] for i in range(299)] + [[50, 100], [150, 200], [250, 290]], 2],  # 2 connected components: [0-1-2-...-49] and [50-100-...-299]
    [500, [[i, i+1] for i in range(499)] + [[100, 150], [200, 250], [300, 350], [400, 450]], 2],  # 2 connected components: [0-1-2-...-99] and [100-150-...-499]
    [1000, [[i, i+1] for i in range(999)] + [[500, 600], [700, 800]], 3],  # 3 connected components: [0-1-2-...-499], [500-600-...-699], and [700-800-...-999]
]

for n,i,x in test_cases:
    print(conn_comp(n,i), x)

p =  [[i, i+1] for i in range(499)] + [[100, 150], [200, 250], [300, 350], [400, 450]]
print(p)
