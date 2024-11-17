def isValid(s):
    print(len(s))
    if len(s)< 2:
        return False
    obj = { ')': '(', ']': '[', '}':'{'}
    stack = []
    for char in s:
        print(char)
        if char in obj:
            print('is in obj', char)
            if stack and stack[-1] == obj[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack

print(isValid(")(){}"))
if []:
    print('it is true')
