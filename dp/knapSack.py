def mx(w,v,c):
    length = len(w)
    def recur(i,cap):
        if i == length:
            return 0
        
        if cap+w[i] <= c:
            return max(v[i]+recur(i+1,cap+w[i]), recur(i+1,cap))
        return recur(i+1,cap)
    ans = 0
    for i in range(length):
        val = recur(i,0)
        if ans < val:
            ans = val

    return ans


print(mx([1,3,4], [15,20,30],4))

print(mx([5,6,7], [10,20,30],4))

print(mx([1,2,3], [10,15,40],6))

print(mx([2,3,4,5], [3,4,5,8],5))
