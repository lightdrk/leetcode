class heap:
    def __init__(self):
        self.root = []

    def parent(self, index):
        return (index - 1) //2

    def left(self, index):
        return ( 2 * index )+1

    def right(self, index):
        return (2 * index )+2

    def heapify_up(self, index):
        while index > 0  and self.root[self.parent(index)] < self.root[index]:
            self.root[self.parent(index)], self.root[index] = self.root[index], self.root[self.parent(index)]
            index = self.parent(index)

    def heapify_down(self, index):
        length = len(self.root)
        left = self.left(index)
        right = self.right(index)
        largest = index
        if left < length and self.root[largest] < self.root[left]:
            largest = left

        if right < length and  self.root[largest] < self.root[right]:
            largest = right

        if largest != index:
            self.root[index], self.root[largest] = self.root[largest], self.root[index]
            self.heapify_down(largest)

    def push(self, val: int):
        self.root.append(val)
        self.heapify_up(len(self.root)-1)

    def pop(self):
        if not self.root:
            return
        val = self.root.pop()
        if self.root:
            self.root[0], val = val, self.root[0]
            self.heapify_down(0)
        return val

    def log(self):
        print(self.root)



arr = [0,1,2,3,4,5,7,8,9]
h = heap()
for n in arr:
    h.push(n)

h.log()
for _ in range(9):
    print(h.pop())
