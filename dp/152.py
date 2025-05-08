def maxProduct(nums):
    length = len(nums)
    output = float('-inf')
    for i in range(length):
        product = 1
        for j in range(i, length):
            product*=nums[j]
            if product > output:
                output = product
    return output


print(maxProduct([3,-1,4]))

def rmaxProduct(nums):
    length = len(nums)
    memo = {}
    ans = float('-inf')
    mn = float('inf')
    mx = float('-inf')
    def recur(i):
        nonlocal ans
        if i >= length:
            return (1, 1)
        if i in memo:
            return memo[i]

        mn, mx = recur(i+1)
        
        mx_m = max(nums[i], nums[i]*mn,nums[i]*mx)
        mn_m = min(nums[i], nums[i]*mn,nums[i]*mx)
        memo[i] = (mn_m,mx_m)
        ans = max(ans,mx_m)
        return (mn_m, mx_m)

    for i in range(length):
        recur(i)
    return ans

print(rmaxProduct([-2,0,-1]))
test = [-3,-1,-1]
print(rmaxProduct(test))
