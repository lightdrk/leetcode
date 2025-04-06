def minSizeSubarray(self, nums: List[int], target: int) -> int:
    length = len(nums)
    nums+=nums
    length+=length
    left = 0
    right = 0
    sm = 0
    ans = float('inf')
    while sm < target and right < length:
        sm+=nums[right%length]
        while sm > target:
            sm-=nums[left%length]
            left+=1
        if sm == target:
            ans = min(ans, right-left+1)
        right+=1
    return ans if ans != float('inf') else -1  
