class heap:
    def __init__(self):
        self.hp = []

    def parent(self, index):
        return (index-1) //2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def heapify(self, index):
