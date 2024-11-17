#possible combinations
nums = [1,2,3]
result = []
def backtracking(index, arr):
    for i in range(index, len(nums)):
        backtracking(i+1,arr)
        arr.append(nums[i])

backtracking(0,[])

print(result)
