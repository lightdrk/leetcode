class heap:
    def __init__(self):
        self.hp = []

    def parent(self, index):
        return (index-1) //2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def heapify_up(self, index):
        while index > 0 and (self.hp[self.parent(index)] > self.hp[index]):
            self.hp[self.parent(index)], self.hp[index] = self.hp[index],  self.hp[self.parent(index)]
            index = self.parent(index)

    def heapify_down(self, index):
        length = len(self.hp)
        small = index
        left = self.left(index)
        right = self.right(index)

        if left < length and (self.hp[left] < self.hp[small]):
            small = left

        if right < length and (self.hp[right] < self.hp[small]):
            small = right

        if small != index:
            self.hp[small], self.hp[index] = self.hp[index], self.hp[small]
            self.heapify_down(small)


    def insert(self, val):
        self.hp.append(val)
        self.heapify_up(len(self.hp)-1)

    def pop(self):
        if len(self.hp) == 0:
            return None

        root = self.hp[0]
        last_element = self.hp.pop()
        if self.hp:
            self.hp[0] = last_element
            self.heapify_down(0)

        return root

    def _print(self):
        print(self.hp)



arr = heap()
arr1 = heap()

for i in [10,5,20,3]:
    arr1.insert(i)

arr1.pop()
arr1._print()

for i in [10, 15, 20, 17, 25]:
    arr.insert(i)

arr.pop()
arr._print()
