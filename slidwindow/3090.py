def maximumLengthSubstring(s: str) -> int:
    window = {}
    output = 0
    left = 0
    for char in s:
        print(window)
        if char in window and window[char] >= 2:
            while s[left] != char:
                window[s[left]]-=1
                left+=1
            window[s[left]]-=1
            left+=1
        if not char in window:
            window[char]=0
        window[char]+=1
        new_out = sum(window.values())
        if output < new_out:
            output = new_out
    return output

print(maximumLengthSubstring("aaaa"))
