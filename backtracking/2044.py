def countbit(nums):
    #hash_map = {}#store our maximum bit or count and maximux bit Or
    store = 0
    mx_t = nums[0]
    for n in nums[1:]:
        mx_t = mx_t | n
    def backtrack(start, current):
        nonlocal store
        if current == mx_t:
            store = store + 1
        for i in range(start, len(nums)):
            backtrack(i+1, current|nums[i])
    backtrack(0,0)
#    for sub in sub_set:
#        if not sub:
#            continue
#        #issue is we should look if any on them doesnt equal to what we want 
#        total = sub[0]
#
#        for i in range(1,len(sub)):
#            total = total | sub[i]
#
#        if total in hash_map:
#            hash_map[total] = hash_map[total] + 1
#        else:
#            hash_map[total] = 1
#
    return store

print(countbit([2,2,2]))
print(countbit([3,2,1,5]))
print(countbit([55525,28668,38258,96251,81200,10371,93505,37010,19127,93921,48740,6582,12557,65216,67792,25652]))
