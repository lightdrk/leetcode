test_case = [[[[1,3],[6,9]],[2,5]],[[[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]]]

def insert(intervals, newInterval):
    left = 0
    right = len(intervals)
    while left < right:
        mid = left + (right-left)//2
        if intervals[mid][1] <= newInterval[0]:
            left = mid+1
        else:
            right = mid
    if intervals[left][0] < newInterval[0] and intervals[left][1] > newInterval[0]:
        intervals[left][1] = max(intervals[left][1],newInterval[1])
    return intervals

for i,n in test_case:
    print(insert(i,n))
