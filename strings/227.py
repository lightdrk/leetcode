'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

    '''


edge_Case = ['1+2+3*2*3/3', '12/2', '2--1','2+-1','2*-1', '2*++-1', '-2', '-2*-1','-1+3']

def func(s):
    nums = []
    neg = False
    multiply = False
    division = False
    i = 0
    while i < len(s):
        if s[i].isdigit():
            number  = 0
            while i < len(s) and s[i].isdigit():
                number = number*10+int(s[i])
                i+=1
            if neg:
                number = -number
                neg = False
            if multiply and nums:
                number*=nums.pop()
                multiply = False
            if division and nums:
                number = int(nums.pop()/number)
                division = False
            nums.append(number)
        else:
            if s[i] == '-':
                neg = True
            elif s[i] == '*':
                multiply = True
            elif s[i] == '/':
                division = True
            i+=1
    return sum(nums)

for s in edge_Case:
    print(func(s))
