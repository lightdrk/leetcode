needle = "issip"
haystack = "mississippi"
left = 0
length = len(needle)
for idx, char in enumerate(haystack):
    if char == needle[left]:
        print(needle[left])
        left+=1
    else:
        left = 0
    if left == length:
        print(idx)
        print(idx - (length -1))
        break


for idx, char in enumerate(haystack):
    if char == needle[0]:
        print(haystack[idx:idx+length])
        if haystack[idx:length] == needle:
            print(idx)
            break
