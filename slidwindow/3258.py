from collections import Counter

def t(s,k):
    count = 0
    c0 = 0
    c1 = 0
    left = 0
    for i in range(len(s)):
        print(count, f'index {i}', f'c0 {c0}', f'c1 {c1}')
        if s[i] == '0':
            c0+=1
        else:
            c1+=1
        while c0>k and c1>k:
            if s[left] == '0':
                c0-=1
            else:
                c1-=1
            left+=1
        count+= i - left + 1

    return count

print(t('10101', 1))
