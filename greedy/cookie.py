def find(g,s):
    g.sort()
    s.sort()
    l = len(s)
    counter = 0
    idx = 0
    for n in g:
        if idx >= l:
            break
        if n <= s[idx]:
            counter+=1
            idx+=1
    return counter

#this above will not work in case of ([2,3,4,5],[2,3,4]) will not work
edge_case = [([1,2,3],[1,2,3]), ([2,1,3], [2,2,2]), ([1,2],[2]), ([1],[3,4]), ([1,2], [])]


def ifind(g,s):
    g.sort()
    s.sort()
    l = len(s)
    counter = 0
    idx = 0
    for n in g:
        if idx >= l:
            break
        if n <= s[idx]:
            counter+=1
            idx+=1
    return counter

for a,b in edge_case:
    print(find(a,b))

