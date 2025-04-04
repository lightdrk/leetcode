def take(s,k):
    length = len(s)
    window = Counter(s)
    if window['a'] < k or window['b'] < k or window['c'] < k:
        return -1
    left = 0
    min_minutes = length 
    count = {'a':0, 'b':0, 'c':0}
    for right in range(length):
        count[s[right]]+=1
        while count['a'] >= k and count['b'] >= k and count['c'] >= k:
            min_minutes = min(min_minutes, right-left+1)
            count[s[left]]-=1
            left+=1
    
    return min_minutes if min_minutes!=length else -1
