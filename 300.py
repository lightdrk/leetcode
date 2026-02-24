test_case = [[10,9,2,5,3,7,101,18],[0,1,0,3,2]]


def length(nums):
    l = len(nums)
    def dp(i):
        if i >= l:
            return 0
        ans = 0
        for idx in range(i+1,l):
            if nums[idx] <= nums[i]:
                continue
            ans = max(ans, 1+dp(idx), dp(idx))
        return ans
    return max(dp(i) for i in range(l))

def lengthTabulation(nums):
    l = len(nums)
    arr = [1]*(l+1)
    arr[l] = 0
    for i in range(l-1,-1,-1):
        ans = 0
        for j in range(i,l):
            if nums[j] > nums[i]:
                ans = max(arr[j]+1,ans)
        arr[i] = ans
    print(arr)
for t in test_case:
    print(lengthTabulation(t))

