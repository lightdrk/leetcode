class Graph:
    def __init__(self, size):
        self.matrix = [[None]*size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        #a to b a->b as directed
        if 0 <= u < self.size and 0 <= v < self.size:
            self.matrix[u][v] = 1

    def add_vertex_data(self, vertex, data):
        #genreally vertex means index in vertex_data
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        for row in self.matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))

        for vertex,data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")


g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)  # A -> B with weight 3
g.add_edge(0, 2)  # A -> C with weight 2
g.add_edge(3, 0)  # D -> A with weight 4
g.add_edge(2, 1)  # C -> B with weight 1

g.print_graph()
