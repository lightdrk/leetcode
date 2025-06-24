from functools import cache

def circular(arr):
    l = len(arr)
    def m(i,l):
        @cache
        def dp(i):
            if i >= l:
                return 0
            return max(arr[i]+dp(i+2), dp(i+1))
        return dp(i)
    return max(m(0,l-1),m(1,l))


print(circular([2,2,3,1,2]))

print(circular([2,2,3,1,2]))

print(circular([2,2,3,1,2]))
