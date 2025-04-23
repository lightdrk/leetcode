def number(s):
    subStr = []
    length = len(s)
    count = 0
    for i in range(length):
        for j in range(i,length+1):
            st = set(s[i:j])
            print(st)
            if 'a' in st and 'b' in st and 'c' in st:
                count+=(length-j+1)
                break

    return count

print(number('abcabc'))
print(number('aaacb'))
print(number('abc'))

