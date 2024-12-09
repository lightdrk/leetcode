#incomplete ...


def largest(nums):
    output = []
    def bkt(start, current):
        if len(current) > 1:
            output.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            bkt(i+1, current)
            current.pop()
    bkt(0,[])
    return output

print(largest([1,2,3]))
