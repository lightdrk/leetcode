test_case = [([1,2,2,2,2,3],2),([1,2,3,4,5,5,5,5,7,7],5)]

def search(t,n):
    left = 0
    right = len(t)-1
    while left < right:
        mid = left + (right-left)//2
        if t[mid] <= n:
            left = mid+1
        else:
            right=mid
    return left

def searchL(t,n):
    left = 0
    right = len(t)-1
    while left < right:
        mid = left + (right-left)//2
        if t[mid] >= n:
            right = mid
        else:
            left=mid+1
    return left


for t,n in test_case:
    print(search(t,n),searchL(t,n))
