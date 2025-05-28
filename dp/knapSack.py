import random

def mxi(w,v,c):
    length = len(w)
    def recur(i,cap):
        if i == length:
            return 0
        
        if cap+w[i] <= c:
            return max(v[i]+recur(i+1,cap+w[i]), recur(i+1,cap))
        return recur(i+1,cap)
    return recur(0,0)


def mx(w,v,c):
    length = len(w)
    cache = {}
    def recur(i,cap):
        if i >= length or cap <= 0:
            return 0
        if (i,cap) in cache:
            return cache[(i,cap)]
        if w[i] > cap:
            cache[(i,cap)] = recur(i+1,cap)
            return cache[(i,cap)]
        cache[(i,cap)] = max(v[i]+recur(i+1, cap-w[i]), recur(i+1,cap))
        return cache[(i,cap)]

    return recur(0,c)

def mxt(w,v,c):
    length = len(v)
    dp = [[0]*(c+1) for _ in range(length)]
    dp[c-w[length-1]][length-1] = val[length]
    for i in range(length-2,-1,-1):
        if w[i] > c-w[i-1]:
            dp[c-]

print(mx([1,3,4], [15,20,30],4))

print(mx([5,6,7], [10,20,30],4))

print(mx([1,2,3], [10,15,40],6))

print(mx([2,3,4,5], [3,4,5,8],5))

print(mx([1,3,4,5], [1,4,5,7], 7))

print(mx([2,2,4,5], [3,7,2,6], 7))

w = [21, 4, 1, 28, 23, 8, 6, 12, 24, 6, 18, 9, 12, 26, 14, 2, 25, 9, 21, 5]
v = [82, 15, 4, 95, 36, 32, 29, 18, 95, 14, 87, 95, 70, 12, 76, 55, 5, 4, 78, 30]
c = 50


print(mx(w,v,c))
print(mxi(w,v,c))

random.seed(10)
w = [random.randint(1,500) for _ in range(300)]
v = [random.randint(1,1000) for _ in range(300)]
c = 200


print(mx(w,v,c))
print(mxi(w,v,c))
