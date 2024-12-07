def subSet(nums):
    #this is a not legit answer but the problem arises 
    #that this does not check for [4,4,4,1] and [4,1,4,4]
    #here this is also wrong 
    #as subset , should include all or any number not the index where they are 
    #is counted
    output = []
    def backtracking(start, current):
        if current[:] not in output:
            output.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            #call backtracking again to check for this point
            #decisions
            backtracking(i+1, current)
            current.pop()
            #not added , we dont need to call backtracking it
            #it is happening in here
    backtracking(0, [])
    return output

print(subSet([4,4,4,1,4]))


def ans(nums):
    nums.sort() #nlogn 
    output = []
    def bc(start, current):
        output.append(current[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                #skip the loop as it is a dup 
                continue
            current.append(nums[i])
            bc(i+1, current)
            current.pop()
    bc(0,[])
    return output


print("correct answer ---->")
print(ans([4,4,4,1,4]))
