def comb(n,k):
    output = []
    def bk(start,curr):
        if len(curr) == k:
            output.append(curr[:])
            return

        for i in range(start,n+1):
            curr.append(i)
            bk(i,curr)
            curr.pop()
    bk(1,[])
    return output

print(comb(5,3))
