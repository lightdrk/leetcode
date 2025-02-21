from collections import deque

def timeRequired(tickets, k):
    que = deque(tickets)
    time = 0
    while que:
        time+=1
        print(k)
        print('?->',que[k])
        ticket = que.popleft()
        ticket-=1
        if ticket == 0 and k == 0:
            return time
        if ticket > 0:
            que.append(ticket)
        if k == 0:
            print(que)
            k = len(que)
        k-=1

print(timeRequired([5,1,1,1],0))

