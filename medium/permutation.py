def p(nums):
    length = len(nums)
    output = []
    def bk(curr):
        output.append(curr[:])
        for i in range(length):
            curr[i],
