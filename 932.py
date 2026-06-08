'''


An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

'''

t = [4,5,6,7,8,9,10]
def proof(arr):
    i=0
    for j in range(2,len(arr)):
        if arr[j-1]*2 == arr[i] + arr[j]:
            return False
        i+=1
    return True

def beautiful(n):
    arr = list(range(1,n))
    def merge(arr):
        l = len(arr)
        if l == 1:
            return arr
        left = merge(arr[:l//2])
        right = merge(arr[l//2:])

        return right+left
    return merge(arr)


for n in t:
    b = beautiful(n)
    print('b ->',b)
    print(proof(b))

