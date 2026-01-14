def hillsVally(arr):
    arr+=[0]
    print(arr)
    hill = 0
    vally = 0
    prev = 0
    for i in range(len(arr)-1):
        if prev < arr[i] and arr[i]> arr[i+1]:
            print(f'hill {prev} {arr[i]} {arr[i+1]}')
            print('Increasing hill countby 1')
            hill+=1
        elif prev >= arr[i] <= arr[i+1]:
            print(f'vally {prev} {arr[i]} {arr[i+1]}')
            vally+=1
        prev = arr[i]

    print(hill,vally)
    return hill+vally

test = [[1,2,0,3,1,1,4]]
for t in test:
    print(hillsVally(t))
