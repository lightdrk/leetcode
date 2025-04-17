def take(s,k):
    length = len(s)
    window = Counter(s)
    if window['a'] < k or window['b'] < k or window['c'] < k:
        return -1
    a = 0
    b = 0 
    c = 0

    return min_minutes if min_minutes!=length else -1
