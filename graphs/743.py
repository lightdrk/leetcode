n = 4
matrix = [[0]*(n+1) for _ in range(n+1)]
times = [[2,1,1],[2,3,1],[3,4,1]]

for i,j,v in times:
    matrix[i][j] = v

print(matrix)

taken = 0

visited = set()
stack = [2]
while stack:
    node = stack.pop()
    if not node in visited:
        visited.add(node)
    for i,v in enumerate(matrix[node]):
        if v:
            stack.append(i)

print(taken)
min_ = 0
def dfs(taken):
    if
