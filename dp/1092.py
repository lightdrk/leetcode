def short(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    great = 0
    small = 0
    ss = ''
    gs = ''
    if l1 > l2:
        great = l1
        gs = s1
        small = l2
        ss = s2
    else:
        great = l2
        gs = s2
        small = l1
        ss = s1
    #for now anything l1 or l2 either of them can be
    def dp(i,j):
        if j >= small:
            return True
        if i >= great and j < small:
            return False

        if gs[i] == ss[j]:
            return dp(i+1,j+1)
        return dp(i+1,j)
    
    if dp(0,0):
        return gs
    #create the dp itself
    def cp(i,j):
        if j >= small:
            return gs
        if i >= great and j < small:
            return gs + ss[j:]
        
        if gs[i] == ss[j]:
            return cp(i+1,j+1)
        return min(ss[j]+ cp(i,j+1), cp(i+1,j), key=len)

    print(cp(0,0))
print(short("abac", "cab"))
