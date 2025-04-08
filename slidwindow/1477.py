def minSum(arr, target):
    length = len(arr)
    ar = []
    for i in range(length):
        for j in range(i,length):
            sm = sum(arr[i:j+1])
            if sm == target:
                ar.append({n for n in range(i,j+1)})
            if sm > target:
                break

    ar.sort(key=len)
    print(ar)
    ans = float('inf')
    for s in ar[1:]:
        if ar[0].isdisjoint(s):
            print(ans)
            ans = min(ans, len(s)+len(ar[0]))
    return ans
print(minSum([2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 20))
        


