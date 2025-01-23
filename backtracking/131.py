def part(s):
    length = len(s)
    output = []
    def bk(ss,start):
        if ss and ss == ss[::-1]:
            output.append(ss)
        for i in range(start, length):
            bk(ss+s[i],i+1)
            print(ss)
    bk('',0)
    return output

print(part('aab'))

