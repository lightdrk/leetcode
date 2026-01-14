test_case = [[1,2,3,7,8,9,4,5,6], [1,2,3,4,5,6], [1,1,1,1,1,2,2,2,3,3,3,5], [-1,-2,-5,10,11],[0,0,-1]]

def selection_sort(arr, reverse=False):
    l = len(arr)
    for i in range(l):
        idx = i
        for j in range(i,l):
            if arr[idx] > arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    return arr
def selection_sort_reverse(arr):
    l = len(arr)
    for i in range(l):
        idx = i
        for j in range(i,l):
            if arr[idx] < arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    return arr

for t in test_case:
    print(selection_sort(t))
    print(selection_sort_reverse(t))

