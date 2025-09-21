'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


'''


'''
edge cases 

-(-3)
--3 ? 
+-
-(2+2)
22+1 
'''

'''
    def calculate(self, s: str) -> int:
        L = len(s)
        def ev(idx):
            ans = 0
            sign = 1
            while idx < L:
                if s[idx].isdigit():
                    num = 0
                    while idx < L and s[idx].isdigit():
                        num = num*10+int(s[idx])
                        idx+=1
                    num*=sign
                    sign = 1 
                    ans += num
                    continue
                elif s[idx] == '(':
                    idx,val = ev(idx+1)
                    ans+=(val*sign)
                    sign = 1
                elif s[idx] == '-':
                    sign*=(-1)
                elif s[idx] == ')':
                    return idx, ans
                idx+=1                

            return idx , ans
        return ev(0)[1]

    '''

def cal(s):
    L = len(s)
    stack = []
    ans = 0
    sign = 1
    idx = 0
    while idx < L:
        if s[idx].isdigit():
            num = 0
            while idx < L and s[idx].isdigit():
                num = num*10+int(s[idx])
                idx+=1
            num*=sign
            sign = 1 
            ans += num
            continue
        elif s[idx] == '(':
            stack.append((ans, sign))
            ans = 0
            sign = 1
        elif s[idx] == ')':
            a,n_sign = stack.pop()
            ans = a + n_sign*(ans*sign)
            sign = 1
        elif s[idx] == '-':
            sign*=(-1)
        idx+=1

    return ans 

edge = ["1 + 1","-(-1)", "(1+(4+5+2)-3)+(6+8)"]
for e in edge:
    print(cal(e))
