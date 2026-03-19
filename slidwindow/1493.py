test_case = [[1,1,0,1],[0,0,0],[1],[0,1,0],[0,1,1,1,0,1,1,0,1],[1,1,1]]

def longestSub(arr):
    left = 0
    count = 0
    largest =0 
    l = len(arr)
    z_count = 0
    for right in range(l):
        if arr[right] == 0:
            z_count += 1
        while z_count >1:
            if arr[left] == 0:
                z_count-=1
            left+=1
        if largest < right-left+1:
            largest = right-left+1
            count = right-left 
    return count

for t in test_case:
    print(longestSub(t))
