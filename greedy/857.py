'''
observations,
1, ration of the wage / quality
2. we have to take maximum of the wage array for distribution , 


'''
import heapq

def func(q,w,k):
    ratio = {j/i for i,j in zip(q,w)}
    ans = float('inf')
    for r in ratio:
        min_heap = []
        for idx,i in enumerate(q):
            i*=r
            if i < w[idx]:
                continue
            #problem is if we push exact then it becomes problematic
            heapq.heappush(min_heap,-i)
            print(min_heap)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            print('after poping -->',min_heap)
        if len(min_heap) == k:
            ans = min(ans,-(sum(min_heap)))
        print('choosen this round --->', ans)

    return ans


test = [[[10,20,5],[70,50,30],2],[[3,1,10,10,1],[4,8,2,2,7],3], [[11,12,5,2,3,31],[10,20,12,13,5,30],4]]

for q,w,k in test:
    print(func(q,w,k))
    print()




