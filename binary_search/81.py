def rotated(arr: list,target):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            return True
        if arr[left] < arr[right]:
            if arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
        elif arr[mid] > arr[left]:
