#brute force solution for this would be a 
def comb(nums, target):
    print("Iterative solution")
    nums.sort()
    stack = [([],target,0)]
    output = []
    while stack:
        arr, diff, idx = stack.pop()
        if diff == 0:
            output.append(arr)
            continue

        for i,n in enumerate(nums[idx:]):
            if diff >= n:
                arr.append(n)
                stack.append((arr[:], diff-n, idx+i ))
                arr.pop()

    return output



print(comb([2,3,6,7], 7))
print(comb([2,3,5], 8))
