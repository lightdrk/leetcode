def longestAlternatingSubarray(nums: list[int], threshold: int) -> int:
    def isOk(nums, l):
        print(nums[0])
        if nums[0] > threshold or nums[0]&1 != 0:
            return False
        for i in range(1,l):
            if nums[i] > threshold:
                return False
            if nums[i-1]&1 == nums[i]&1:
                return False
        return True
    length = len(nums)
    l_len = 0
    for i in range(length):
        for j in range(i,length):
            l = j+1 - i
            print(isOk(nums[i:j+1], l),l)
            if isOk(nums[i:j+1], l):
                l_len = max(l_len, l)
    return l_len


print(longestAlternatingSubarray([3,2,5,4],5))
