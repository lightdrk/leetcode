def fsa(nums):
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            hash_map[nums[i]]['f'] = 1 + hash_map[nums[i]]['f']
            hash_map[nums[i]]['index'].append(i)
        else:
            hash_map[nums[i]] = {'f':1, 'index': [i]}
    freq = 0

    for n in hash_map:
        freq = max(freq, hash_map[n]['f'])
    length = len(nums)
    for n in hash_map:
        if hash_map[n]['f'] == freq:
            length = min(length, len(nums[hash_map[n]['index'][0]:hash_map[n]['index'][-1] + 1]))
    return length

print(fsa([1,2,2,3,1]))
print(fsa([1,2,2,3,1,4,2]))
print(fsa([1]))
print(fsa([1,2]))
