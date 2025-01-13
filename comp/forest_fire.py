for x,y,i in [[1,2,3],[2,3,4]]:
	print(x,y,i)

graph = [[0]*6 for _ in range(6)]
arr = [[1,2,5],[2,3,8],[1,5,10]]
for x,y,w in arr:
	graph[x][y] = w

print(graph)
