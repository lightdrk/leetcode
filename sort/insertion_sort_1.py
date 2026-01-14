test_case = [[1,2,3,7,8,9,4,5,6], [1,2,3,4,5,6], [1,1,1,1,1,2,2,2,3,3,3,5], [-1,-2,-5,10,11],[0,0,-1]]

def insertion_sort(arr):
    l = len(arr)
    for i in range(l):
        key = arr[i]
        j = i-1
        while 0 <= j and arr[j] >= key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr


for t in test_case:
    print(insertion_sort(t))
