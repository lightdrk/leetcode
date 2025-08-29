def func(nums):
    nums.sort()
    l = len(nums)
    ans = set()
    for i in range(l):
        if i > 0 and nums[i-1] == nums[i]:
            print('skip?')
            continue
        hash_map = {}
        for j in range(i+1,l):
            if ( 0 - nums[i] - nums[j] ) in hash_map:
                ans.add((nums[i], (0-nums[i]-nums[j]), nums[j]))
            hash_map[nums[j]] = 1

    return list(ans)

def funcO(nums):
    nums.sort()
    l = len(nums)
    ans = []
    for i in range(l):
        if i > 0 and nums[i-1] == nums[i]:
            print('skip?')
            continue
        hash_map = {}
        for j in range(i+1,l):
            print(j)
            if j > i+2 and nums[j-1] == nums[j]:
                continue
            if ( 0 - nums[i] - nums[j] ) in hash_map:
                ans.append([nums[i], (0-nums[i]-nums[j]), nums[j]])
            hash_map[nums[j]] = 1

    return ans
edge_case = [[0,0,0,0,0,0], [-1,0,1], [1,1,1],[-1,0,1,2,-1,-4] ]

def funcT(nums):
    nums.sort()
    l = len(nums)
    ans = []
    for i in range(l):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        left = i +1
        right = l-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                ans.append([nums[i],nums[left], nums[right]])
                left+=1
                right-=1
            elif total > 0:
                right-=1
                while left < right and nums[right] == nums[right+1]:
                    right-=1
            else:
                left+=1
                while left < right and nums[left] == nums[left-1]:
                    left+=1
    return ans 
for nums in edge_case:
    #print(func(nums))
    #print(funcO(nums))
    print(funcT(nums))
