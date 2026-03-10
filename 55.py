test_case = [[3,2,1,0,4],[1,2,0,0,5], [1,2,3,0,5], [2,3,1,1,4], [0], [0,1]]

def canJump(arr):
    nj = 0
    for i,n in enumerate(arr):
        if nj < i+n:
            nj = i+n
        if nj == i:
            return False
    return True

for t in test_case:
    print(canJump(t))

''' above would not work as it is checking at current time , it works if current is being looked but what if nj crosses the current this happens , when we
are starting from zero , and starting itself is zero and this condition is by passed, giving wrong answer. '''
'''
another issue with this algo is that starting value itself is the end meaning arr has length of 1 then we need to add extra guards which is un neccessary
'''

def canJumpV2(arr):
    nj = arr[0]
    for i in range(1,len(arr)):
        if nj < i:
            return False
        nj = max(nj,i+arr[i])
    return True

for t in test_case:
    print(canJumpV2(t))
