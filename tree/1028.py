test_case = ['1-2--3--4-5--6--7', '1-2--3-5--6--7']



for s in test_case:
    depth = 0

    left = 0
    for i in range(len(s)):
        if s[left] != '-':
            left+=1
        if s[i] != '-':
            left = i
        depth = max(depth, i-left+1)

    print(depth)
    lvl_order = [[] for _ in range(depth+1)]
    print(lvl_order)
    depth_c = 0
    for char in s:
        if char.isnumeric():
            lvl_order[depth_c].append(int(char))
            depth_c = 0
        else:
            depth_c+=1

    print(lvl_order)



