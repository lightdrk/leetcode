'''
Each element in the subarray has a weight associated with it. The weight for each index is given in another array, weights. Find the subarray of length 
𝑘
k that has the maximum weighted average.

Problem Statement:
Given two arrays nums and weights of equal length and an integer 
𝑘
k, find a contiguous subarray of length 
𝑘
k that has the maximum weighted average:

Weighted Average
 
Return this value.

'''

def weightedAvg(nums: list[int], weight: list[int], k: int) ->float:
    sum_of = sum([nums[i]*weight[i] for i in range(k)])
    s = sum_of

    for i in range(len(nums)-k):
        s = sum_of - nums[i]*weight[i] + nums[k+i]*weight[k+i]
        sum_of = max(sum_of, s)
    return s/k

print(weightedAvg([1,12,-5,-6,50,3], [2,1,1,1,2,1], 3))
