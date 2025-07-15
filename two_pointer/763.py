def partion(s):
    last_occur = {char: idx for idx,char in enumerate(s)}
    left= right = 0
    ans = []
    for idx in range(len(s)):
        char = s[idx]
        right = max(right, last_occur[char])
        
        if idx == right:
            ans.append(right-left+1)
            left = idx+1

    return ans

print(partion("aAbBcCaA"))
