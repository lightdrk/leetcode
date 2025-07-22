'''
🧠 Problem Statement:
You are given:

A list of items where each item has a weight and a value.

A knapsack that can carry at most W weight.

But here’s the twist:
You are allowed to take fractions of items.

Your task is to maximize the total value in the knapsack.
'''
#input [(value,weight)]
def kp(arr: list[tuple[int,int]], weight):
    arr.sort(key= lambda x: x[0]/x[1],reverse=True)
    ans = 0
    for val, wei in arr:
        if weight == 0:
            return ans
        #5 - 2 == 3
        #0+val added..
        #weight = 3
        #else
        #2 - 5 = -3
        #ans = 10/5 * 2
        #weight = 0
        if weight-wei >= 0:
            ans+=val
            weight-=wei
        else:
            ans+=(val/wei)*(weight)
            weight=0
    return ans

print(kp([(5,2),(10,5),(100,5)],7))
print(kp([(5,2)],7))
print(kp([(5,200)],7))
print(kp([(1,1),(1,1),(1,1)],7))
print(kp([(5,1),(100,3)],7))
print(kp([(5,1),(100,3)],1))

