'''

You are given a binary array nums.

A subarray of an array is good if it contains exactly one element with the value 1.

Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

'''


def func(arr):
    l = len(arr)
    def recur(i):
        if i >= l:
            return 1
        if arr[i] == 1:
            ans = 1
            print(ans)
            while i < l-1 and arr[i+1] != 1:
                ans+=recur(i+1)
                i+=1
            print(ans)
            return ans + recur(i+1)
        return recur(i+1) 
    return recur(0)


print(func([0,1,0,0,1]))
    

