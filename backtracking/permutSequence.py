def swap(s,i,j):
    s = list(s)
    s[i],s[j] = s[j], s[i]
    return ''.join(s)

def seq(n,k):
    s = ''
    for i in range(1,n+1):
        s = s + str(i)
    print(s)
    def back(start,current):
        if n-1 == start:
            if k == 0:
                s = current
        for i in range(start, n):
            current = swap(current,start,i)
            back(start+1, current)
            current = swap(current,start,i)
    back(0,s)
    return s

print(sorted(seq(3,6)))
