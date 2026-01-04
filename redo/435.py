'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
    '''

def erase(intervals):
    intervals = sorted(intervals,key= lambda x : x[1])
    print(intervals)
    ans = 0
    t = intervals[0][1]
    for start,end in intervals[1:]:
        if t > start:
            ans+=1
            continue
        t = end
    return ans

test_case = [[[1,2],[2,3],[3,4],[1,3]],[[1,2],[1,2],[1,2]],[[1,2],[3,4],[3,5],[4,5]]]

for t in test_case:
    print(erase(t))
