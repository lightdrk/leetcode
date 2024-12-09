def next_p(nums):
    def back(start,current):
        nonlocal nums
        if len(nums) == start:
            print(current[:])
            nums = current[:]
        for i in range(start,len(nums)):
            current[start], current[i] = current[i], current[start]
            if start <= 1:
                back(start+1, current)
            else:
                return
    back(0,nums)
    return nums

print(next_p([1,2,3]))
print(next_p([2,3,1]))
print(next_p([3,2,1]))
print(next_p([1,1,5]))
