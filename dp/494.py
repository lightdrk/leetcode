'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

'''
#thoughts:

'''
question was kinda easy if we went with the flow ..
we had to do two recursion one with + expression and another with - expression 
we evaulate it as we go if length == idx then simply check if target == ans
'''
#stuck
'''
i was kinda stuck at createing a map of how to approach this ... 
in terms of recursion 
no i just need to upgrade it to memoization ..


'''

def fd(nums, target):
    length = len(nums)
    memo = {}
    def recur(i,ans):
        if i >= length:
            return 1 if target == ans else 0
        if (i,ans) in memo:
            return memo[(i,ans)]
        memo[(i,ans)] = recur(i+1,ans+nums[i]) + recur(i+1, ans-nums[i])
        return memo[(i,ans)]
    return recur(0,0)

