#V1
def generate(n):
    par = ['(',')']
    output = []

    def isValid(s):
        st = []
        for char in s:
            if char == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    return False
            else:
                st.append(char)
        return not st

    def bk(s):
        if len(s) == n*2:
            if isValid(s):
                output.append(s)
            return
        for i in range(2):
            bk(s+par[i])

    bk('')
    return output
print(generate(3))




#V2
def generateV2(n):
    output = []
    def bk(s,oc,cc):
        if len(s) == n*2:
            output.append(s)
            return
        if oc < n:
            bk(s+'(',oc+1,cc)
        if cc < oc:
            bk(s+')',oc,cc+1)

    bk('',0,0)
    return output
print(generateV2(3))
