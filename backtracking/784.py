def letterCasePermute(s :str) ->list[str]:
    length = len(s)
    output = []
    def bk(idx, ss):
        output.append(ss)
        for i in range(idx,length):
            print(idx)
            if not ss[i].isnumeric():
                char = ss[i]
                if not char.islower():
                    char = char.casefold()
                else:
                    char = char.upper()
                bk(i+1,ss[:i]+char+ss[i+1:])


    bk(0, s)
    return output

print(letterCasePermute('a1b2'))
