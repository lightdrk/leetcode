'''
2[a3[2[b]]]

2[a3[bb]]
2[abbbbbb]
abbbbbbabbbbbb

    '''


def func(strings):
    count_stack = []
    s_stack = []
    curr_num = 0
    curr_str = ''
    for s in strings:
        if s.isdigit():
            curr_num = curr_num*10 + int(s)
        elif s == '[':
            count_stack.append(curr_num)
            s_stack.append(curr_str)
            curr_num = 0
            curr_str = ''
        elif s == ']':
            repeat = count_stack.pop()
            prev_str = s_stack.pop()
            curr_str = prev_str+ curr_str*repeat
        else:
            curr_str+=s
    return curr_str

print(func('2[a3[2[b]]]'))


