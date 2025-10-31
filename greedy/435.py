'''
non-overlapping intervals


'''

def over(intervals):
    l = len(intervals)
    def dp(idx):
        if idx >= l:
            return 0

        a = intervals[idx]
        output = 0
        for i in intervals[idx+1:]:
            if i[0] < a[1]:
                output+=1
        return output+dp(idx+1)
    return dp(0)
edge = [[[[1,2],[2,3],[3,4],[1,3]]]]

print(over(edge[0]))
