def selection_sort(arr: list[int]):
    l = len(arr)
    for i in range(l):
        idx = i
        for j in range(i+1,l):
            if arr[i] < arr[j]:
                idx = j
        arr[i],arr[idx] = arr[idx],arr[i]
    return arr




def insertion_sort(arr):
    l = len(arr)
    for i in range(1,l):
        key = arr[i]
        while i >= 0 or arr[i-1] > key:
            arr[i] = arr[i-1]
            i-=1

    return arr


test = [[1,3,2,4,5,6]]

for t in test:
    print(selection_sort(t))
    print(insertion_sort(t))
