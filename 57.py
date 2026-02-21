test_case = [
        [[[1,3],[6,9]],[2,5]],
        [[[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]],
        [[[1,2],[2,3],[6,9],[10,13]], [3,5]],
        [[[1,2],[3,4],[4,6]],[7,9]],
        [[[1,3],[7,8]],[4,6]],
        [[[1,2],[3,5]],[5,7]],
        [[[1,5]],[0,3]],
        [[[5,7]],[0,4]],
        [[[3,5],[6,7]],[0,10]],
        [[[3,5],[6,7]],[0,6]],
        [[[2,3],[5,7]],[0,6]]
        ]

def insert(intervals, newInterval):
    left = 0
    right = l = len(intervals)
    while left < right:
        mid = left + (right-left)//2
        if intervals[mid][1] < newInterval[0]:
            left = mid+1
        else:
            right = mid
    arr = []
    if left >= l:
        return intervals+[newInterval]
    if (intervals[left][0] <= newInterval[0] <= intervals[left][1]) :
        print('mergeing?')
        intervals[left][1] = max(intervals[left][1],newInterval[1])
        arr.append(intervals[0])
        for start,end in intervals:
            if arr[-1][1] > start:
                continue
            if arr[-1][1] == start:
                arr[-1][1] = end
                continue
            arr.append([start,end])
        return arr
    elif (newInterval[0] < intervals[left][0] <= newInterval[1]):
        intervals[left][0] = newInterval[0]
        intervals[left][1] = max(newInterval[1],intervals[left][1])
        arr.append(intervals[0])
        for start,end in intervals:
            if arr[-1][1] > start:
                continue
            if arr[-1][1] == start:
                arr[-1][1] = end
                continue
            arr.append([start,end])
        if arr[-1][1] > intervals[-1][0]:
            arr[-1][1] = max(intervals[-1][1],arr[-1][1])
        return arr
    for i in range(l):
        if i == left:
            arr.append(newInterval)
        arr.append(intervals[i])
    return arr 

def insert_v2(intervals,newInterval):
    #this is as intervals are already sorted by start time
    #as given in the question 
    #also start > end
    left = 0
    right = l = len(intervals)
    while left < right:
        mid = left+(right-left)//2
        if intervals[mid][0] < newInterval[0]:
            left = mid+1
        else:
            right = mid

    arr = intervals[:left]+[newInterval]+intervals[left:]
    output = [arr[0]]
    for s,e in arr[1:]:
        if output[-1][1] >= s:
            output[-1][1] = max(output[-1][1],e)
            continue
        output.append([s,e])
    return output


for i,n in test_case:
    print(insert_v2(i,n))
