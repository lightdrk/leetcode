def generate(n):
    par = ['(']*n + [')']*n
    output = []
    def bk(s,start,st):
        if len(s) == n*2 and not st:
            print(s)
            output.append(s)
            return
        for i in range(start,n*2):
            char = par[i]
            if st and char == ')' and st[-1] == '(':
                st.pop()
                bk(s+char,start+1,st)
                st.append('(')
            else:
                st.append(char)
                bk(s+char,start+1,st)
                st.pop()

    bk('',0,[])
    return output

print(generate(3))
