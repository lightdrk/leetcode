def single(nums):
    result = 0
    for i in nums:
        result = result ^ i
        print('--->',result)

    return result

print(single([2,3,4,2,1]))

print(single([2,1,3]))
