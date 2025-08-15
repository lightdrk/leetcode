def func(grid):
    l = len(grid[0])
    prefix = [[0]*l, [0]*l]
    for i in range(2):
        for j in range(l):
            prefix[i][j] = prefix[i][j-1]+grid[i][j]

    print(prefix)
    b = 0
    mx = float('-inf')
    for t in range(l):
        print(f'**********{t}**************')
        a = prefix[0][t]+ prefix[1][l-1]
        print(a)
        if t > 0:
            print(f'{a} - {prefix[1][t-1]}', a-prefix[1][t-1])
            a-=prefix[1][t-1]
        print(a)
        if mx < a:
            mx = a
            b = t
    print(b)
    if b == 0:
        return  prefix[0][l-1] - prefix[0][b]
    return max(prefix[0][l-1] - prefix[0][b], prefix[1][b-1])

print(func([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]))


