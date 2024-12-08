def swap(s,i,j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)


def permuteString(s: str) ->list[str]:
    permutations = []
    def backtracking(start,current):
        if start == len(s)-1:
            permutations.append(current)
            return 
        for i in range(start, len(s)):
            current = swap(current, start, i)
            backtracking(start+1, current)
            current = swap(current,start,i)
    backtracking(0,s)
    return permutations

print(permuteString('abc'))

def permute(nums):
    permut = []
    length = len(nums)
    def back(start, current):
        if start == length - 1:
            permut.append(current[:])
            return
        for i in range(start, length):
            current[start],current[i] = current[i], current[start]
            print(current)
            back(start+1, current)
            current[start],current[i] = current[i], current[start]
            print(current)
    back(0,nums)
    return permut


print(permute([1,2,3]))
