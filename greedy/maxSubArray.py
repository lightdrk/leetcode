def mx(nums: list[int]):
    '''
        kandane algo 
        intuition is that 
            if we shuold include current val num or start a new 

        '''
    mx = ans = nums[0]
    for num in nums[1:]:
        ans+=num
        if ans < num:
            ans = num
        if mx < ans:
            mx = ans

    return mx

''' what if we want index too? '''

def idmx(nums: list[int]) ->tuple[int,int]:
    '''
        this gives us sub array too
    '''
    mx = ans = nums[0]
    start = end = s = 0
    for i,num in enumerate(nums[1:],1):
        ans+=num
        if ans < num:
            ans = num
            s = i

        if mx < ans:
            mx = ans
            start = s
            end = i
    return (start, end)


print(idmx([-2,1,-3,4,-1,2,1,-5,4]))


