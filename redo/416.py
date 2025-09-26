'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

    '''
'''
if constrains are both pasiting and neg then does our approach of checking if we have total sum as odd or even works


'''

'''
1,2,1,-2
1,2,1,-1,-1
-1,-1
'''
'''
total sum we need to get
check if its odd or not or lenth arry should < 2 return False
if sum == 0:
 half = 0
else
    half the sum

recursion , params essentiall will be curr diff, and idx
base case:
    if diff == 0:
        return True
    if diff < 0 or idx > len:
        return False
return recur(idx+1,half-curr[idx]) or recur(idx+1, half)
'''

edge_case = [[1,1,2,1], [2,2], [4], [3], [], [1,-1],[0,0,0,0]]

'''
harder if both +, - are allowed with empty subset as true meaning empty subset [] [] == 0
then we will have empty subset as empty 
'''

def md(arr):
    l = len(arr)
    if l == 0:
        return True
    sm = sum(arr)

    if sm == 0:
        return True
    if sm&1 == 1 or l < 2:
        return False
    half = sm//2
    def dp(idx,total):
        if total == 0:
            return True
        if total < 0 or idx >= l:
            return False
        return dp(idx+1,total-arr[idx]) or dp(idx+1,total)
    return dp(0,half);


for arr in edge_case:
    print(md(arr))
