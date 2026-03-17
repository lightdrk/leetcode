from collections import deque

test_case = [([2,1,1,1,4],3),([1,2,1,1,4],3),([1,2,1,1,1],3), ([1,1,4,1,1],2),([2,2,2,1,2,2,1,2,2,2],2)]
ans = [4,2,3]


'''
def nS(nums,k):
    def atMost(arr,k):
        l = len(arr)
        left = 0
        odd = 0
        count = 0
        for right in range(l):
            odd+=(arr[right]&1)
            while odd >=k:
                count+=(l-right)
                odd-=(arr[left]&1)
                left+=1
        return count
    return atMost(nums,k-1)-atMost(nums,k)


above atmost logic is wrong lol done for atleast logic 
'''

def nS(nums,k):
    def atmost(nums,k):
        l = len(nums)
        left = 0
        odd = 0
        count = 0
        for right in range(l):
            odd+=(nums[right]&1)
            while odd > k:
                odd-=(nums[left]&1)
                left+=1
            count+=(right-left+1)
        return count
    return atmost(nums,k)-atmost(nums,k-1)

def nS_v2(nums,k):
    #thoughts , 
    # we can do someting like , loop , add when count of odd exceeds k
    # adjust window srink window , 
    #then add a condition on odd == k , count even numbers before first odd
    left = 0
    l = len(nums)
    count = 0
    odd = 0
    fo = []
    for right in range(l):
        odd+=(nums[right]&1)
        while odd > k:
            odd-=(nums[left]&1)
            left+=1
        if odd == k:
            count+=1
            n = left
            while nums[n]&1 == 0:
                count+=1
                n+=1
    print(count)
    return count

def nS_v3(nums,k):
    #thoughts , 
    # we can do someting like , loop , add when count of odd exceeds k
    # adjust window srink window , 
    #then add a condition on odd == k , count even numbers before first odd
    left = 0
    l = len(nums)
    count = 0
    odd = 0
    fo = deque()
    for right in range(l):
        if nums[right]&1:
            odd+=1
            fo.append(right)

        while odd > k:
            odd-=(nums[left]&1)
            if fo[0]<=left:
                fo.popleft()
            left+=1

        if odd == k:
            count+=(fo[0]-left+1)

    return count


def nS_v4(nums,k):
    #use prefix sum 
    hash_map = {0:1} #base case because we start from zero 
    prefix = 0
    count = 0
    for n in nums:
        prefix+=(n&1)
        count+=(hash_map.get(prefix-k,0))
        hash_map[prefix] = hash_map.get(prefix,0)+1
    return count





for t,k in test_case:
    #print(nS(t,k))
    print(nS_v3(t,k)== nS_v4(t,k))
