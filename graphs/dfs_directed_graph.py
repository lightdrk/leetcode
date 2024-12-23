class Graph:
    def __init__(self,size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, v,u):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dfs_utils(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v])
        for i in range(len(self.matrix[v])):
            if self.matrix[v][i] == 1 and not visited[i]:
                self.dfs_utils(i, visited)

    def dfs_recursive(self, vertex_start):
        visited = [False] * self.size
        self.dfs_utils(self.vertex_data.index(vertex_start), visited)


    def dfs(self, start: str) -> None:
        #start = 'A'
        stack = [self.vertex_data.index(start)]
        visited = [False] * self.size
        while stack:
            root = stack.pop()
            if not visited[root]:
                visited[root] = True
                print(self.vertex_data[root], end=" ")
            for i in range(len(self.matrix[root])):
                if self.matrix[root][i] == 1 and not visited[i]:
                    stack.append(i)


g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.dfs('A')

