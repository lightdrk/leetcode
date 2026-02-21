test_cases = [
[[1,3],[2,6],[8,10],[15,18],[11,13]],
[[1,3],[3,5],[5,100]],
[[0,10],[0,100],[100,101],[1,20]],
[[1,4],[1,4]]

        ]

def merge(intervals):
    #as intervals are jumbled and not in order then we short by start tiem
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    arr = [intervals[0]]
    for s,e in intervals[1:]:
        if arr[-1][1] >= s:
            arr[-1][1] = max(e,arr[-1][1])
            continue
        arr.append([s,e])
    return arr



for t in test_cases:
    print(merge(t))
