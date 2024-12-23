def combine(candidates, target):
    output = []
    def bk(start,current):
        if sum(current) == target:
            output.append(current[:])
        if sum(current) > target:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            bk(i, current)
            current.pop()
    bk(0,[])
    return output

print(combine([2,3,6,7], 7))
