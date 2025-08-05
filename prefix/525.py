'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

'''

def func(arr):
    prefix = 0 
    count = 0
    hash_map = {0:-1} 
    for i, n in enumerate(arr):
        prefix+=n
        if n == 0:
            prefix-=1

        if prefix in hash_map:
            count = max(count,i-hash_map[prefix])
        else:
            hash_map[prefix] = i

    return count

'''
above works for [0,1] binary array what if 
question becomes like their will be no binary array rather will be any numeber from -inf to +inf, but constrains are same equal number of 0 and 1 ,

then we can still do above alog with a twist of cheking if number is not 1 or zero then skip it 
then above logic holds
    '''

def func(arr):
    prefix = 0 
    count = 0
    hash_map = {0:-1} 
    for i, n in enumerate(arr):
        if n == 0:
            prefix-=1
        if n == 1:
            prefix+=1

        if prefix in hash_map:
            count = max(count,i-hash_map[prefix])
        else:
            hash_map[prefix] = i

    return count


case = [[1,2,34,0], [1,1,2,0,2,1,0,0,2]]
for t in case:
    print(func(t))
