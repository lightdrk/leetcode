class PN:
    def __init__(self):
        self.arr = []

    def add(self,num):
        self.arr.append(num)
    def getProduct(self,k):
        prod = 1
        for n in self.arr[:k]:
            prod*=n
        return prod
