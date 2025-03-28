from collections import Counter

def longestNiceSubstring(s: str) -> str:
    length = len(s)
    longest = ''
    for i, char in enumerate(s):
        for j in range(i,length):
            string = s[i:j+1]
            window = Counter(string.lower())
            if not 1 in window.values():
                print(string)
                if len(string) > len(longest):
                    longest = string
    return longest

print(longestNiceSubstring("dDzeE"))
