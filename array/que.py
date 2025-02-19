from collections import deque
que = deque()
print(not que)
for i in range(5):
    que.append(i)
print(que)
last = -1
arr = deque()
while que:
    if last != -1:
        arr.append(last)
    last = que.popleft()

print(last)
print(arr)

