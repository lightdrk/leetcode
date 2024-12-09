
####not complete 47

def permuteDupless(nums):
    nums.sort()
    print(nums)
    length = len(nums)
    permute = []
    def back(start, current):
        if length == start:
            permute.append(current[:])
            return
        for i in range(start, length):
            if i > start and nums[i] == nums[i-1]:
                continue
            current[start], current[i] = current[i], current[start]
            back(start+1, current[:])
            current[start], current[i] = current[i], current[start]
    back(0,nums)
    return permute

print(permuteDupless([1,1,2]))
print(permuteDupless([1,2,3]))
print(permuteDupless([3,2,1]))
print(permuteDupless([0,1,0,0,9]))
