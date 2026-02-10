test_case = [[1,2,3,7,8,9,4,5,6], [1,2,3,4,5,6], [1,1,1,1,1,2,2,2,3,3,3,5], [-1,-2,-5,10,11],[0,0,-1]]

def bubble_sort(arr):
    l = len(arr)
    for _ in range(l):
        isSwapped = False
        idx = 0
        while idx < l-1:
            if arr[idx] > arr[idx+1]:
                isSwapped=True
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            idx+=1
        if not isSwapped:
            break
    return arr

for t in test_case:
    print(bubble_sort(t))
