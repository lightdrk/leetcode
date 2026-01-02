'''
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
'''

def findTheCity(n,edges,dist):
    graph = {}
    for f,t,d in edges:
        if f not in graph:
            graph[f] = []
        if t not in edges:
            graph[t] = []
        graph[f].append((t,d))
        graph[t].append((f,d))
    cities = n
    ans = 0
    for i in range(n):
        print(f'Starting City {i}')
        stack = [(i,0)]
        path = set()
        while stack:
            print(stack)
            city,d = stack.pop()
            path.add(city)
            for node,distance in graph[city]:
                if distance+d <= dist:
                    stack.append((node,distance+d))
        t = len(path)
        print(t)
        if cities >= t:
            cities = t
            ans = max(ans,i)
    return ans


test_case = [[4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4], [5,[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2]]
for n,e,d in test_case:
    print(findTheCity(n,e,d))
