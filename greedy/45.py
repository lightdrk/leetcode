'''

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

'''


def func(nums):
    l = len(nums)
    '''
        @cache
        def dp(i):
            if i >= l-1:
                return 0
            reach = i+nums[i]
            if reach >= l-1:
                return 1
            step = float('inf')
            for j in range(1,nums[i]+1):
                if j + i < l and reach < j+i+nums[j+i]:
                    step = min(step,1+dp(i+j))

            return step

        return dp(0)
        '''
    '''
        dp = [float('inf')]*(l)
        dp[l-1] = 0
        for i in range(l-2,-1,-1):
            reach = i+nums[i]
            if reach >= l-1:
                dp[i] = 1
            else:
                for j in range(1,nums[i]+1):
                    if j+i < l-1 and reach <j+i+nums[j+i]:
                        dp[i] = min(dp[i],1+dp[i+j])

        return dp[0]
        '''
    '''
        1. we simply add 1 when we reach the end to step 
        2. we only add or use the thing if we can go beyond nums[i] . 
            so choices we have for us is those which increase the jump longest
            question here: should how can increase the jump or how to take max between 
                on the fly i am thinking of taking , in range kind of thing . 
        '''
    '''
        1 we start , then we take max between start+1 , end of nums[start] with index

    '''


