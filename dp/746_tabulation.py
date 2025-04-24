def cst(cost):
    m1 = cost[0]
    m2 = cost[1]
    for i in range(2,len(cost)):
        tmp = cost[i] + min(m1, m2)
        m1 = tmp
        m2,m1 = m1,m2

    return min(m1,m2)

print(cst([10,15,20]))
print(cst([1,100,1,1,1,100,1,1,100,1]))
