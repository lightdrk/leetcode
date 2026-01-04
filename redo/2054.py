'''

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.


'''
def binary(arr,right,val):
    left = 0
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid][0] <= val:
            left = mid+1
        else:
            right = mid-1

    return right

def maxTwo(events):
    events.sort()
    l = len(events)
    ans = 0
    for i in range(l):
        _, end, value = events[i]
        high = 0 
        start = binary(events,l-1,end)
        for s,e,v in events[start+1:]:
            high = max(high,v)
        ans = max(ans,high+value)
    return ans








test_case = [[[1,3,2],[4,5,2],[2,4,3]],[[1,3,2],[4,5,2],[1,5,5]],[[1,3,2],[4,5,2],[2,4,3]]]

for t in test_case:
    print(maxTwo(t))
