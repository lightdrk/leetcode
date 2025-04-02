def maxVowels(s :str, k :int)->int:
    vowels = {'a','e','i','o','u'}
    count = 0
    for i in range(k):
        if s[i] in vowels:
            count+=1
    if count == k:
        return k
    left = 0
    for right in range(k,len(s)):
        print(f'right {right}', f'left {right-k}', f'count {count}')
        if s[right-k] in vowels:
            count-=1
        if s[right] in vowels:
            count+=1

    return count

print(maxVowels("weallloveyou", 7))
print()
print(maxVowels("abciiidef", 3))
