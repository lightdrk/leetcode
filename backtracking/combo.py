def combination(n,k):
    #combination of [1,n] where number of number present is k
    #so n = 3, and k = 3 then [1,2,3], [1,3,3] etc
    #we can not have same combination like [1,3,2] or [1,2,3] both are same
    output = []
    def bk(start, curr):
        if len(curr) == k:
            output.append(curr[:])
            return
        for i in range(start,n+1):
            curr.append(i)
            bk(i+1,curr)
            curr.pop()
    bk(1,[])
    return output

print(combination(5,3))
