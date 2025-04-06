from collections import Counter 

def countGood(nums: list[int], k):
    def isGood(count):
        g = 0
        for n in count:
            g+=((count[n]-1)*count[n]//2)
            if g >= k:
                return True
        return False

    good = 0
    count = {}
    left = 0
    length = len(nums)
    for i in range(length):
        if not nums[i] in count:
            count[nums[i]]=0
        count[nums[i]]+=1
        print(count)
        while isGood(count):
            print('True',count)
            good+=1
            left+=1
            count[nums[left]]-=1
    return good

print(countGood([1,1,1,1,1],10))
print(countGood([3,1,4,3,2,2,4],2))
