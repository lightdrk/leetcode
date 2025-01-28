def sub(arr :list[int], k :int, threshold :int) -> int:
    count = 0
    window = 0
    length = len(arr)
    for i in range(k):
        window+=arr[i]
    if window//k >= threshold:
        count+=1

    for i in range(k,length):
        window-=arr[i-k]-arr[i]
        if window//k >= threshold:
            count+=1


    return count
print(sub([2,2,2,2,5,5,5,8],3,4))

print(sub([11,13,17,23,29,31,7,5,2,3],3,5))
