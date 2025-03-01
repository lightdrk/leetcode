from collections import Counter
import heapq

def least(tasks, n):
    counter = Counter(tasks)
    heap = []
    interval=0
    for task in counter:
        for t in heap:
            if t[0] > 0:
                t[0]-=1
        interval+=1
        counter[task]-=1
        heapq.heappush(heap, [n,task])
    print(counter)
    print(heap)
    while heap:
        time, task = heapq.heappop(heap)
        if time == 0:
            counter[task]-=1
            if counter[task] > 0:
                heapq.heappush(heap, [n,task])
            interval+=1
        else:
            print('1')
            heapq.heappush(heap,[time-1, task])


    return interval

print(least(["A","A","A","B","B","B"],2))
