def eval(tokens):
    stack = []
    for n in tokens:
        print(stack)
        try:
            stack.append(int(n))
        except:
            second = stack.pop()
            first = stack.pop()
            if n == '+':
                first+=second
            elif n == '-':
                first-=second
            elif n == '*':
                first*=second
            else:
                first/=second
            stack.append(int(first))
    return stack[0]


print(eval(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

