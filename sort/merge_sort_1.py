test_case = [[1,2,3,7,8,9,4,5,6], [1,2,3,4,5,6], [1,1,1,1,1,2,2,2,3,3,3,5], [-1,-2,-5,10,11],[0,0,-1]]

def merge_sort_1(arr):
    l = len(arr)
    if l < 2:
        return arr
    left = merge_sort_1(arr[:l//2])
    right = merge_sort_1(arr[l//2:])
    i=j=0
    if not left:
        return right
    if not right:
        return left
    result = []
    while i < len(left) and j < len(right):
        if left[i]>right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

for t in test_case:
    print(merge_sort_1(t))
