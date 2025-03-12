from collections import deque

def min_time_taken(times: list[list[int]], n, k):
    matrix = [[0]*(n+1) for _ in range(n+1)]
    for i,j,v in times:
        matrix[i][j] = v
    print(matrix)
    visited = set()
    min_t = 99999999999
    que = deque([])
    que.append((k, 0))
    while que:
        print(que)
        source, taken = que.popleft()
        if not source in visited:
            min_t = taken
            visited.add(source)
        for i, val in enumerate(matrix[source]):
            if val and not i in visited:
                que.append((i,taken+val))
                matrix[source][i] = 0
    return -1 if len(visited) != n else min_t

testCases =testCases = [
    ([[2,1,1], [2,3,1], [3,4,1]], 4, 2),  # Test case 1
    ([[1,2,1]], 2, 2),  # Test case 2
    ([[1,2,1], [2,3,2], [1,3,4]], 3, 1),  # Test case 3
    ([[1,2,2], [2,3,3], [3,4,4], [4,5,5]], 5, 1),  # Test case 4
    ([[1,2,5], [1,3,3], [3,4,2], [2,4,1]], 4, 1),  # Test case 5
    ([[1,2,1], [1,3,1], [2,3,1]], 3, 1),  # Test case 6
    ([[1,2,2], [1,3,1], [2,3,1], [3,4,2]], 4, 1),  # Test case 7
    ([[1,2,1], [1,3,2], [3,2,2]], 3, 1),  # Test case 8
    ([[1,2,10], [2,3,1], [3,4,1], [4,5,1]], 5, 1),  # Test case 9
    ([[1,2,3], [2,3,1], [1,3,5]], 3, 1),  # Test case 10
]


for test, n, k in testCases:
    print(min_time_taken(test,n,k))

