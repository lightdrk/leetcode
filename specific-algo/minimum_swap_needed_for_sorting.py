'''
minimum swap needed to sort the array 
[1,6,2,3,5] ==> [1,2,3,5,6]
swaps required ??
'''


def swaps_required(array):
    arr = {j:i for i,j in enumerate(sorted(array))}
    visited = [False]*len(array)
    swaps = 0
    for i, val in enumerate(array):
        if visited[i] or i == arr[val]:
            continue
        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr[val]
            cycle_len+=1
        if cycle_len>1:
            swaps+=(cycle_len-1)
    print(swaps)


case = [[2,3,1], [4,1,2,3], [1,5,4,3,2], [10,11,5,6], [7,8,9], [7, 6, 8, 5]]

for a in case:
    swaps_required(a)


def func(array):
    sorted_map = {val: i for i, val in enumerate(sorted(array))}
    swaps = 0
    visited = [False]*len(array)
    for i,val in enumerate(array):
        if visited[i] or i == sorted_map[val]:
            continue
        stack = [(i,val)]
        sw = 0
        while stack:
            idx, v = stack.pop()
            if visited[idx]:
                continue
            visited[idx] = True
            sw+=1
            stack.append((sorted_map[v],v))

        if sw > 1:
            swaps+=(sw-1)

    return swaps
print("**************************************")
for a in case:
    print(func(a))
