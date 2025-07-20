hash = {}
arr = [1, 2, -3, 3, -1, 2, -2]
sm = 0
ans = 0
for i,n in enumerate(arr):
    sm+=n
    if sm == 0:
        ans = i+1
    if sm in hash:
        ans = max(ans, i-hash[sm]+1)
    hash[sm] = i

print(ans)
