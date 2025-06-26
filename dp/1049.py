'''
 You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

'''

'''
Instead of simulating the smashing process (which is messy), you transform the problem into this:
Split the stones into two groups, such that the absolute difference of their total weights is minimised.
Now how to solve this?'''
        #return should be twice of s1


'''

def last(stones):
    length = len(stones)
    sm = sum(stones)
    def recur(i,s1):
        if i >= length:
            return abs(sm - 2*s1)
        
        return min(recur(i+1,s1+stones[i]), recur(i+1,s1))
    return recur(0,0)

print(last([2,7,4,1,8,1]))
print(last([31,26,33,21,40]))

