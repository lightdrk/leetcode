test_case = [[1,3,0,1,4], [0,0,5], [1], [1,1,1,1,1,1,5]]

def jump(arr):
    l = len(arr)
    if (l == 1):
        return 0
    cache = [None]*l
    def dp(i):
        steps = arr[i]+ i 
        if steps >= l-1:
            return 0
        if cache[i]:
            return cache[i]
        ans = float('inf')
        for j in range(i+1,steps+1):
            ans = min(ans,dp(j))
        cache[i] = 1+ans
        return cache[i]
    gg = dp(0)+1
    print(cache)
    return gg

#TAbulation
def tabulation(arr):
    l = len(arr)
    cache = [float('inf')]*l
    cache[l-1] = 0


def idea(arr):
    ans = 0
    l = len(arr)
    i=0
    while i<l-1:
        steps = arr[i] + i
        if steps >= l-1:
            return ans
        new = i
        prev = 0
        for j in range(i+1,steps+1):
            if prev<arr[j]:
                new = j
        if new > i:
            ans+=1
        else:
            return -1
        i=new
    return ans+1

def idea2(arr):
    ans = 0
    l = len(arr)
    idx = 0
    mx = arr[idx]+idx
    while idx < l-1:
        steps = arr[idx]+idx
        if steps >= l-1:
            return ans+1 
        i = idx+1
        while i <= steps:
            mx = max(mx,nums[i]+i)
            i+=1


for t in test_case:
    print(idea(t))
