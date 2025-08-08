'''
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

'''
'''
brilliant question very simple solution i am in awe
like 
we simple loop and calcaulte if we hit tank < 0 then we reset the start to i+1 and tank empty as we are starting an new 

'''

def func(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    l = len(cost)
    for i in range(l):
        tank+=gas[i]-cost[i]
        if tank < 0:
            start = i+1
            tank = 0

    return -1 if start >= l else start
