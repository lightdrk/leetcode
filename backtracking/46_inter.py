def it(nums):
    stack = [0]
    length = len(nums)
    output = []
    while stack:
        i = stack.pop()
        if i == length-1:
            output.append(nums[:])
        for j in range(i,length):
            nums[i],nums[j] = nums[j],nums[i]
            stack.append(i+1)
            nums[i],nums[j] = nums[j],nums[i]

    return output


print(it([1,2,3]))
