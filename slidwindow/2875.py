def minSizeSubarray(nums: list[int], target: int) -> int:
    length = len(nums)
    prefix = [0]*length
    for i,n in enumerate(nums):
        prefix[i] = n + prefix[i-1] 

    while 


print(minSizeSubarray([1,2,2,2,1,2,1,2,1,2,1], 83))
print(minSizeSubarray([1,2,3],5))
print(minSizeSubarray([1,1,1,2,3],4))
print(minSizeSubarray([2,4,6,8],3))

