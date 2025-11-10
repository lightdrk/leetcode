'''
Problem: Charging Stations on a Highway

You are driving on a long straight highway represented by an integer array stations, where each element stations[i] indicates the maximum number of kilometers your car can travel after recharging at station i.

You start at station 0, and your goal is to reach the final station (n - 1). From any station i, you may drive to any next station j such that:

j > i

j - i <= stations[i]

Return the minimum number of recharges needed to reach the final station.
It is guaranteed that the destination is reachable.

'''

'''
can we carry forward the charge ? , -> no

    '''
'''
[3,2,1,1,4]

[3,3,1,1,4]
[3,2,3,1,4]
[3,1,3,2,4,5]

    '''
test_case = [[3,2,1,1,5],[3,3,1,1,4],[1],[3,2,3,1,4],[3,1,3,2,5,4], [2,3,1,1,1,4],[1,1], [2,3,0,1,4], [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]]

'''
def gd(arr):
    #Fails for many overcounts 
    jump = 0
    beyond = arr[0]
    l = len(arr)
    for i in range(1,l):
        if beyond >= l-1:
            jump += 1
            break
        if beyond < i+arr[i]:
            beyond = i+arr[i]
            jump +=1
    return jump
'''

def gd(arr):
    jump = 0
    beyond = 0
    end = 0
    l = len(arr)
    for i in range(l-1):
        beyond = max(beyond, i + arr[i])
        if end == i:
            end = beyond
            jump+=1
    return jump



for t in test_case:
    print(gd(t))



