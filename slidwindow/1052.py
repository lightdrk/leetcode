def maxSat(customers, grumpy, minutes):
    length = len(customers)
    if length<=minutes:
        return sum(customers)
    left = 0
    count = 0
    cust = 0
    ans = 0
    r = 0
    l = 0
    for right in range(length):

        if grumpy[right]:
            count+=1
        cust+=customers[right]
        while count >= minutes:
            if grumpy[left]:
                count-=1
            cust-=customers[left]
            left+=1
        if ans < cust:
            ans = cust
            r = right
            l = left

        print(f'cust -> {cust}')
        print(f'ans -> {ans}')
        print(f'count -> {count}')
    print(f'l --> {l}')
    print(f'r --> {r}')
    for i in range(l):
        if not grumpy[i]:
            cust+=customers[i]
    for j in range(r,length):
        if not grumpy[j] or (grumpy[j] == 1 and  count <= minutes):
            cust+=customers[j]
            count+=1
    return cust 

print(maxSat([5,8,9], [0,1,1],1))
