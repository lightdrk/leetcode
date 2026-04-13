"""
There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

Return the maximum number of customers that can be satisfied throughout the day.


"""








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

#print(maxSat([5,8,9], [0,1,1],1))


"""

this code below fails where if , we are checking we should have atleast one count of one in grumpy, but
this idea fails as if we had only limited number of ones  last case on the test_Case is edge case for the code

def g(customers,grumpy,minutes):
    l = len(grumpy)
    left = -1
    for i in range(l):
        if grumpy[i]:
            left = i
            break
    if left == -1:
        return sum(customers)
    count_one = customers[left:left+minutes].count(1)
    window = sum(customers[left:left+minutes])
    mx = window
    start = left
    for right in range(left+minutes,l):
        if grumpy[left]:
            count_one-=1
        if grumpy[right]:
            count_one+=1
        window+=(customers[right]-customers[left])
        left+=1
        if count_one == 0:
            continue
        if mx < window:
            mx = window
            start = left 

    print(start)
    ans = 0
    for i in range(l):
        if grumpy[i] and (i > start or i < start+minutes):
            continue
        ans+=customers[i]
    return ans


test_case = [[[1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3],[[1],[0],1],[[1,0,1,2,1,1,7,5],[0,1,0,1,0,0,0,0],3]]

for t in test_case:
    print(g(t[0],t[1],t[2]))

"""

test_case = [[[1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3],[[1],[0],1],[[1,0,1,2,1,1,7,5],[0,1,0,1,0,0,0,0],3],[[5,5,5,7,1,2,3,4,5,13],[1,1,1,1,0,0,1,0,0,1],3]]



def g(customers,grumpy,minutes):
    ln = len(grumpy)
    left = 0
    sm=ans = 0
    g = 0
    l=r=0
    for right in range(ln):
        if grumpy[right]:
            g+=1
        ans+=customers[right]
        while g and right-left+1 > minutes:
            if grumpy[left]:
                g-=1
            ans-=customers[left]
            left+=1
        if sm < ans:
            sm = ans
            l = left
            r = right
    return ans+sum(customers[:l])+sum(customers[r:])

for t in test_case:
    print(g(t[0],t[1],t[2]))




















