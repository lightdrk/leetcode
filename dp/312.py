'''
def maxCoins(nums):
    def recur(nums):
        length = len(nums)
        if length == 0:
            return 0
        ans = 0
        for i in range(length):
            out = nums[i]
            if i-1 > -1:
                out*=nums[i-1]
            if i+1 < length:
                out*=nums[i+1]
            new = nums[:]
            new.pop(i)
            out+=recur(new)
            if ans < out:
                ans = out

        return ans
    
    return recur(nums)

print(maxCoins([3,1,5,8]))
print(maxCoins([7,9,8,0,7,1,3,5,5,2,3]))
print(maxCoins([1]))
print(maxCoins([1,2]))
print(maxCoins([1,5]))
'''
'''
single index can not give all possibility...single index can not give all possibility...  

❌❌❌❌❌❌❌❌❌❌❌
def maxCoins(nums):
    length = len(nums)
    def recur(i):
        if i >= length:
            return 0
        answer = 0
        ans = nums[i]
        if i-1 > -1:
            ans*=nums[i-1]
        if i+1 < length:
            ans*=nums[i+1]
        new = nums[:i]+nums[i+1:]
        l = len(new)
        for j in range(l):
            out=recur(i+j)
            if answer < out:
                answer = out

        return ans+answer
    
    return recur(0)


print(maxCoins([3,1,5,8]))
'''


def maxCoins(nums):
    nums = [1]+nums+[1]
    length = len(nums)
    def recur(left,right):
        if left+1 == right:
            return 0
        ans = 0
        for i in range(left+1,right):
                ''' 
                here left and right are far beacuse we are solving the problem in between first 
                which removes them so left and i and right becomes neighbours
                '''
            coins = nums[left]*nums[i]*nums[right]
            coins+=recur(left,i) + recur(i,right)

            if ans < coins:
                ans = coins

        return ans

    return recur(0,length-1)

print(maxCoins([3,1,5,8]))
print(maxCoins([7,9,8,0,7,1,3,5,5,2,3]))
print(maxCoins([1]))
print(maxCoins([1,2]))
print(maxCoins([1,5]))
