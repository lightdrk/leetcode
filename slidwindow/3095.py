def minimumSubarrayLength(nums: list[int], k: int) -> int:
    length = len(nums)
    ans = float('inf')
    output = []
    for i in range(length):
        for j in range(i,length):
            output.append(nums[i:j+1])
    for arr in output:
        curr = 0
        for n in arr:
            curr|=n
        if curr >= k:
            ans = min(ans,len(arr))
    return ans if ans != float('inf') else -1
print(minimumSubarrayLength([16,1,2,20,32],45))
