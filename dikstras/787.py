import heapq

def findCheapestPrice( n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int|float:
        #can not go stop > k
    matrix = [[-1]*n for _ in range(n)]
    for f, t, p in flights:
        matrix[f][t] = p
    print(matrix)
    price = [float('inf')]*n
    visited = [False]*n
    pr = [(0,src,0)]
    while pr:
        print(pr)
        cost, node, stops = heapq.heappop(pr)
        if stops>k:
            continue
        for i, c in enumerate(matrix[node]):
            if c != -1:
                cst = cost+c
                if price[i] > cst:
                    price[i] = cst
                    heapq.heappush(pr,(cst,i, stops+1))
    print(price)
    return price[dst] if price[dst] != float('inf') else -1


#print(findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))
#print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
#print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
#print(findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))
print(findCheapestPrice(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))
#778. Swim in Rising Water
#815. Bus Routes
#1091. Shortest Path in Binary Matrix
#1631. Path With Minimum Effort
#2812. Find the Safest Path in a Grid
#2642. Design Graph With Shortest Path Calculator
