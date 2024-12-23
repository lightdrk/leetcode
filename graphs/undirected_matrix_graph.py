class Graph:
    def __init__(self,size):
        #here size means number of nodes
        self.adj_matrix = [[0]*size for _ in range(size)]#[[0,0,0],[0,0,0],[0,0,0]] => size -> 3
        self.size = size
        self.vertex_data = ['']*size #=> ['', '', ''] => size -> 3,

    def add_edge(self, u, v):
        #u and v are edges connecting like a -> b where a -> m[0][] and b -> m[1][] 
        #[[0,1,0][1,0,0]] a-b connected
        if 0 <= v < self.size and 0 <= u < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1


    def add_vertex_data(self,vertex, data):
        #this is used to name the node in graph case vertex, 
        #vertex is index
        # data is string name 'A'
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))

        for vertex, data in enumerate(self.vertex_data):
            print(f'Vertex {vertex}: {data}')


g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2)

g.print_graph()
