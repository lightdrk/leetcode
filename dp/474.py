'''
was able to do it , had an issue of making arr as none
because i was appending to array which returns none
cause whole function to crash... had to chatgpt it ....

Also this problem is realted to knapsack , need to read about it for dp conversion ...
i did convert it but eitheir giving wrong answer or timeout if place wrongly ...

'''


def findMaxForm(strs: list[str], m: int, n: int) -> int:
    length = len(strs)
    ans = [0]
    def recur(arr, i, mi, ni):
        if i == length:
            if mi <= m and ni <= n:
                ans[0] = max(ans[0], len(arr))
            return
        recur(arr+[strs[i]], i+1, mi+strs[i].count('0'), ni+strs[i].count('1'))
        recur(arr, i+1, mi, ni)
    recur([],0,0,0)
    return ans[0]


print(findMaxForm(["10","0001","111001","1","0"],5,3))
strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
m = 9
n = 80
print(findMaxForm(strs,m,n))
