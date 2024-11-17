def fib(n):
    #this is not a dp  it i sjust recursion and not efficent
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#here it is saving with n as key and f(n-1) + f(n-2) result as value
memo = {} # this is for memorization 
def fb(n, memo):
    #dp with resurice approach or top down method
    # here it is saving with n as key and f(n-1) + f(n-2) result as value
    if memo.get(n):
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1

    # this will append or add the result to memo for memorization
    memo[n] = fb(n-1, memo) + fb(n-2, memo)
    return memo[n]


print('this is using recursion ---->',fib(19))
print('this is using dp top to bottom or top down appraoc --->', fb(19, memo))

def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n+1) #[0,0,....n index]
    dp[1] = 1
    for i in range(2,n+1):  # start from 2 as 1 is already in
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print('this is using dp with bottom up approach --->', f(19))
