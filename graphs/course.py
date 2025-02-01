def possible(courses,pre):
    graph = {i:[] for i in range(courses)}
    for course,p in pre:
        graph[p].append(course)
    print(graph)
    def cycle(i):
        if visited[i] == 2:
            return True
        elif visited[i] == 1:
            visited[i] = 2
        else:
            visited[i] = 1
        for n in graph[i]:
            if cycle(n):
                return True
        return False
    visited = [0]*courses
    for i in range(courses):
        if visited[i] == 0:

            print(cycle(i))

print(possible(5,[[1,4],[2,4],[3,1],[3,2]]))
