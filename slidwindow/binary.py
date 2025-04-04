def binary(arr: list[int], num: int, right: int):
    left = 0
    right = len(arr)
    while left<right:
        mid = left + (right-left)//2
        #print(mid, right)
        diff = num - arr[mid]
        if -2 <= diff <= 2:
            return arr[mid]
        elif diff > 2:
            right=mid-1
        elif diff < -2:
            left=mid+1
    return -1


print(binary([3,4,7,8], 3,5))

