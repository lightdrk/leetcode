'''
array is circular , we an not rob 0 and last this will cause alarm

'''

def rob(nums):
    length = len(nums)
    def recur(i,j):
        if i >= length-j:
            return 0
        
        return nums[i]+recur(i+2,j)

    return max(recur(0,1),recur(1,0))

print(rob([2,3,2]))
print(rob([1,2,3,1]))

