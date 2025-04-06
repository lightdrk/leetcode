from collections import defaultdict 

def countGood(nums: list[int], k):
    good = 0
    count = defaultdict(int)
    p_count=0
    left = 0
    length = len(nums)
    for right in range(length):
        count[nums[right]]+=1
        if count[nums[right]]>1:
            p_count+=(count[nums[right]]-1)
        print(f'p_count: {p_count}',f'good: {good}')
        while p_count >= k and left < right:
            good+=(length-right)
            print(f'good += {length-right}', f'p_count>=k: {p_count>=k}')
            if count[nums[left]] > 1:
                p_count-=(count[nums[left]]-1)

            count[nums[left]]-=1
            left+=1
    return good

#print(countGood([1,1,1,1,1],10))
print(countGood([1,1,3,1,2,1,2,2,1,2,1,2,3,3],14))

