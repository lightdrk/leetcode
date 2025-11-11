def decode(s):
    l = len(s)
    def recur(i):
        num = 0 
        string = ''
        while i < l:
            if s[i].isdigit():
                while s[i].isdigit():
                    num = num*10 + int(s[i])
                    i+=1
            elif s[i] == '[':
                ans,idx = recur(i+1)
                ans*=num
                num = 0
                string+=ans
                i = idx+1
            elif s[i] == ']':
                return string,i
            else:
                string+=s[i]
                i+=1
        return string
    return recur(0)
def decodeS(s):
    l = len(s)
    nums = []
    num = 0
    string = ''
    strings = []
    i=0
    while i < l:
        if s[i].isdigit():
            num = num*10+int(s[i])
            i+=1
        elif s[i] == '[':
            nums.append(num)
            num = 0
            strings.append(string)
            string = ''
            i+=1
        elif s[i] == ']':
            string*=nums.pop()
            string = strings.pop() + string
            i+=1
        else:
            string+=s[i]
            i+=1
    return string

test = ["3[a]2[b]","33[a20[b[cd]]]", "3[a]2[bc]","3[a2[c]]","2[abc]3[cd]ef","aa[2[a]]","2[a]3[c]"]
for t in test:
    print(decode(t) == decodeS(t))
