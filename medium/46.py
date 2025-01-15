def permute(nums: list[int]) -> list[list[int]]:
    length = len(nums)
    output=[]
    def bk(curr,start):
        if start == length-1:
            output.append(curr[:])
            return
            for i in range(start, length):
                curr[i],curr[start] = curr[start],curr[i]
                bk(curr,start+1)
                curr[i],curr[start] = curr[start],curr[i]
    bk(nums,0)
    return output

print(permute([1,2,3]))

