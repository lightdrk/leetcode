#rotated sorted array
def search(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = left + (right-left)
        if arr[left] < target and target < arr[mid]:
            if arr[left]<=arr[mid] and arr[mid] > target:
                right = mid+1
            else:
                left = mid
        else:
            left = mid
