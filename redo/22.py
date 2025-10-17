'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


    '''
def generate(n):
    output = []
    def bk(o,c,s):
        if o == c == n:
            output.append(s)
            return

        if o < n:
            bk(o+1,c,s+'(')
        if c < o:
            bk(o,c+1,s+')')

    bk(0,0,'')
    return output


def generateI(n):
    output = []
    stack = [(0,0,'')]
    while stack:
        o,c,s = stack.pop()
        if o == c == n:
            output.append(s)
            continue
        if c < o:
            stack.append((o,c+1,s+')'))
        if o < n:
            stack.append((o+1,c,s+'('))

    return output

'''
what if we have 3 otptions for like (, { , [

'''
def generateT(n):
    output = []
    closing = {'(':')','{':'}','[':']'}
    def bk(s,o={'(':0, '{': 0,'[': 0},c={'(':0, '{': 0,'[': 0}):
        if sum(o.values()) == sum(c.values()) == n*3:
            output.append(s)
            return 
        for i in ['(', '[','{']:
            if o[i] < n:
                o[i]+=1
                bk(s+i,o,c)
                o[i]-=1
            if c[i] < o[i]:
                c[i]+=1
                bk(s+closing[i],o,c)
                c[i]-=1
    bk('')
    return output

edge = [1,2]
for t in edge:
    print(generateT(t))
