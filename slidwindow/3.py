'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def h(s):
    if len(s) == 1:
        return 1
    high =0
    window = ""
    for i in s:
        print(window)
        if i in window:
            high = max(high, len(window))
            print(high)
            window = i
            continue
        window = window + i
    print(high)
    return len(window)

print(h("aba"))

