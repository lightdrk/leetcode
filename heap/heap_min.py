class heap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index-1)//2

    def left(self, index):
        return (index*2) + 1

    def right(self, index):
        return (index*2) + 2

    def heap_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def heap_down(self, index):
        length = len(self.heap)
        smallest = index
        left = self.left(index)
        right = self.right(index)
        if left < length and self.heap[smallest] > self.heap[left]:
            smallest = left

        if right < length and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heap_down(smallest)

    def insert(self, val):
        self.heap.append(val)
        self.heap_up(len(self.heap) - 1)

    def pop(self):
        val = self.heap.pop()
        if self.heap:
            self.heap[0], val = val, self.heap[0]
            self.heap_down(0)
        return val

    def peek(self):
        return self.heap[0]

    def log(self):
        print(self.heap)


arr = [0,1,2,3,4,5,7,8,9]
h = heap()
for n in arr[::-1]:
    h.insert(n)

h.log()
for _ in range(9):
    print(h.pop())




