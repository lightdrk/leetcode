'''
💼 Meeting Rooms II
You are given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i].

Each interval represents a meeting with a start and end time.

🔸 Your task: Return the minimum number of meeting rooms required so that no meetings overlap in the same room.

🧠 Example:
python
Copy
Edit
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation:

Meeting 1: 0 to 30

Meeting 2: 5 to 10 (overlaps with Meeting 1)

Meeting 3: 15 to 20 (also overlaps with Meeting 1)

At most, 2 meetings overlap at the same time, so we need 2 rooms.

'''
import heapq

def func(arr: list[list[int]]):
    if not arr:
        return 0
    arr.sort(key=lambda x: x[0])
    minHeap = []
    ans = 0
    for start,end in arr:
        while minHeap and start >= minHeap[0]:
            heapq.heappop(minHeap)
        
        heapq.heappush(minHeap, end)
        ans = max(ans,len(minHeap))

    return ans

print(func([[0,10],[10,20]]))
print(func([]))
print(func([[0, 30], [5, 25], [10, 20]]))
