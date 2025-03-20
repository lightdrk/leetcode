#brute force approach not usefull, n**2
def equal_to_zero(arr):
    for i,n in enumerate(arr):
        curr = 0
        for n in arr[i:]:
            curr+=n
            if curr == 0:
                return True
    return False


print(equal_to_zero([1,2,3,-1,1]))

print(equal_to_zero([1,2,3,-1,-1]))

#prefix sum optimized

def equal_pref(arr):
    prefix = {}
    prev = 0
    for n in arr:
        prev+=n
        if prev in prefix:
            return True
        prefix[prev] = 1
    return False

print(equal_pref([1,2,3,-1,1]))

print(equal_pref([1,2,3,-1,-1]))
