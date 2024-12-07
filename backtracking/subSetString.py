def ss(s):
    result = []

    def bk(start, current):
        result.append(''.join(current[:]))
        for i in range(start,len(s)):
            current.append(s[i])
            bk(i+1, current)
            current.pop()

    bk(0,[])
    return result

print(ss("abcd"))
