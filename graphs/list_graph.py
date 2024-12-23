class Graph:
    def __init__(self):
        self.graph = {}

    def add_edges(self, vertex, edge):
        if edge in self.graph:
            self.graph[vertex].append(edge)

    def add_vertices(self, vertices):
        if vertices not in self.graph:
            self.graph[vertices] = []

    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                print(vertex, end=" ")
            for neighbor in vertex:
                if neighbor not in visited:
                    stack.append(neighbor)

