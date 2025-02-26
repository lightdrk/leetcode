class heap:
    def __init__(self):
        self.hp = []

    def parent(self, index):
        return (index - 1)//2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def heapify_up(self, index):
        while index > 0 and (self.hp[self.parent(index)] < self.hp[index]):
            self.hp[self.parent(index)],  self.hp[index] = self.hp[index], self.hp[self.parent(index)]
            index = self.parent(index)

    def heapify_down(self, index):
        length = len(self.hp)
        largest = index
        left = self.left(index)
        right = self.right(index)

        if left < length and (self.hp[largest] < self.hp[left]):
            largest = left

        if right < length and (self.hp[largest] < self.hp[right]):
            largest = right

        if largest != index:
            self.hp[largest], self.hp[index] = self.hp[index], self.hp[largest]
            self.heapify_down(largest)



    def insert(self, val):
        print(self.hp)
        self.hp.append(val)
        self.heapify_up(len(self.hp) - 1)

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

arr = [0,1,2,3,4,5,7,8,9]
h = heap()
for n in arr:
    h.insert(n)

h._print()
for _ in range(9):
    print(h.pop())
