'''

You are given an array of meeting time intervals where each interval is represented as intervals[i] = [start_i, end_i]. Each interval indicates when a meeting starts and ends. Return the minimum number of conference rooms required to schedule all the meetings without any conflicts. In other words, if two or more meetings overlap, each requires its own room.
    '''
import heapq

def func(meeting):
    heap = []
    meeting.sort(key=lambda x: x[0])
    rooms = 0
    for start,end in meeting:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        else:
            rooms+=1

        heapq.heappush(heap,end)
    return rooms


print(func([[0,50],[5,10],[15,20],[25,30],[35,40]]))  # Expected 2
print(func([[0,5],[0,10],[0,15]]))  # Expected 3
print(func([[0,30],[5,10],[15,20]]))  # Expected 2
print(func([[0,10],[15,20]]))  # Expected 1
print(func([[0,30],[5,10],[6,11],[7,12]]))  # Expected 4
print(func([[0,30]]))  # Expected 1
print(func([[0,300],[10,200], [20,200], [30,200]]))  # Expected 4


def funcMeet(meeting):
    heap = []
    meeting.sort(key=lambda x: x[0])
    for start,end in meeting:
        ans = [end,[[start,end]]]
        if heap and heap[0][0] <= start:
            ans = heapq.heappop(heap)
            ans[0] = end
            ans[1].append([start, end])
        heapq.heappush(heap,ans)

    return [x[1] for x in heap]

print(funcMeet([[0,50],[5,10],[15,20],[25,30],[35,40]]))  # Expected 2
print(funcMeet([[0,5],[0,10],[0,15]]))  # Expected 3
print(funcMeet([[0,30],[5,10],[15,20]]))  # Expected 2
print(funcMeet([[0,10],[15,20]]))  # Expected 1
print(funcMeet([[0,30],[5,10],[6,11],[7,12]]))  # Expected 4
print(funcMeet([[0,30]]))  # Expected 1
print(funcMeet([[0,300],[10,200], [20,200], [30,200]]))  # Expected 4

