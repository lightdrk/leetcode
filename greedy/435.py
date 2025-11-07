'''
non-overlapping intervals


'''
'''

#    first attempt

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
'''

def over(intervals):
    l = len(intervals)
    def dp(i):

        #if over lap -> 1+dp(i+1,)
        #remove at ever overlap dp(i+1,)

edge = [[[[1,2],[2,3],[3,4],[1,3]]]]

print(over(edge[0]))
