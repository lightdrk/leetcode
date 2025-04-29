def numberOfSub(nums,k):
    odd = 0
    left = 0
    count = 0
    length = len(nums)
    for right in range(length):
        if nums[right]&1:
            odd+=1
        while odd==k:
            if odd == k:
                count+=1
            if nums[left]&1:
                odd-=1
            left+=1

    return count


print(numberOfSub([1,1,2,1,1],3))
print(numberOfSub([2,2,2,1,2,2,1,2,2,2],2))
