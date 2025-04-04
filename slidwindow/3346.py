from collections import Counter

def maxFreq(nums: list[int], k: int, numOperations: int)->int:
    #get a counter
    #get counter in sorted array to find most likley to be changed or operated towards
    #we have {1: 4, 3: 2, 0:1: 5: 5},,
    #we can use either 5 or 1 depending on what k is 
    #we have to change maximum one 
    #if we are not able to do any operations on max we move to other one
    #after getting a sorted arry or freq , we will choose to do operations on most closest to be converted
    ''' 
        1. we will not be able to reach high freq num or any num
            ->we will check diff max diff by adding or subing to all
        2. we can reach a freq but can not reach still the max default freq
            -> we will check by adding the number of operations we can do 
        3. we can increase the freq of high

    '''
    def binary(arr: list[int], num: int, right: int):
        left = 0
        right = len(arr)
        while left<right:
            mid = left + (right-left)//2
            #print(mid, right)
            diff = num - arr[mid]
            if -k <= diff <= k:
                return arr[mid]
            elif diff > k:
                right=mid-1
            elif diff < -k:
                left=mid+1
        return -1

    freq_c = Counter(nums)
    #print(f'frequency counter -> {freq_c}')
    mx_val, mx_f = 0,0
    for val, freq in freq_c.items():
        if mx_f < freq:
            mx_f = freq
            mx_val = val

    t = True
    for n,f in freq_c.items():
        if mx_f - f < numOperations and mx_val - n <= k:
            t = False
            break
    if t:
        return freq

    arr = []
    length = 0
    for n in freq_c:
        length+=1
        arr.append(n)
    arr.sort()
    for i,n in enumerate(arr):
        no = 0
        idx = i+1
        while -1 < no < numOperations and idx < length :
            val = binary(arr[idx+1:], n, length-idx+1)
            if val == -1:
                break
            no+=freq_c[val]
            idx+=1
        freq_c[n]+=no - (no - numOperations)
    #print(freq_c)
    return max(freq_c.values())


print(maxFreq([1,4,5],1,2))
print(maxFreq([5,11,20,20],5,1))
