class numArray:
    def __init__(self, arr :list[int]):
        self.nums = []
        pref = 0
        for n in arr:
            pref+=n
            self.nums.append(pref)

    def sumRange(self, i, j):
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i-1]


x = numArray([-2, 0, 3, -5, 2, -1])

print(x.sumRange(2,5))
