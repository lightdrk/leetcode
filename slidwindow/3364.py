def minSubSumArray(nums, l, r):
    min_ = sum(nums[:l])
    min_sum = min_
    length = len(nums)
    print(length-2)
    for i in range(1,length-1):
        min_+=nums[i+1] - nums[i-1]
        if min_ < 0:
            continue
        if min_sum > min_:
            min_sum = min_
    return min_sum

a = [3,-2,1,4]

minSubSumArray(a,2,3)
