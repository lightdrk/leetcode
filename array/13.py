def romanToInt(s: str) -> int:
    hash = { 'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    num = 0
    prev = 1000
    for char in s:
        curr = hash[char]
        if  prev < curr:
            curr-=2*prev
        num+=curr
    return num
