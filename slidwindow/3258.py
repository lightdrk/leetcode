def t(s,k):
    length = len(s)
    count = 0
    for i in range(length):
        print(i)
        c1 = 0
        c0 = 0
        for j in range(k*2+1):
            if i+j >= length:
                break
            print(i+j)
            if s[i+j] == '0':
                c0+=1
            else:
                c1+=1
            if c1 <= k and c0 <= k:
                count+=1
    return count

print(t('10101', 1))
