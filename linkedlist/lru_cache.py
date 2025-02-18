print('v1 Try LRU CACHE')
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.root = None

    def get(self, key: int) ->int:
        if not key in self.map:
            return -1
        if self.root.val == key:
            return self.map[key]

        tmp = self.root
        while tmp.next and (tmp.next.val != key):
            tmp = tmp.next
        node = tmp.next
        tmp.next = tmp.next.next
        node.next = self.root
        self.root = node
        return self.map[key]

    def put(self, key: int, value: int) ->None:
        if key in self.map:
            self.map[key] = value
            if self.root.val == key:
                return
            node = Node(key)

            tmp = self.root
            while tmp.next and tmp.next.val != key:
                tmp = tmp.next
            tmp.next = tmp.next.next
            node.next, self.root = self.root, node
            return

        node = Node(key)
        if self.cap:
            node.next = self.root
            self.root = node
            self.map[key] = value
            self.cap-=1
        else:
            tmp = self.root
            if not tmp.next:
                self.map.pop(tmp.val)
                self.root = node
                self.map[key] = value
            else:
                while tmp.next and tmp.next.next:
                    tmp = tmp.next
                print(self.map)
                self.map.pop(tmp.next.val)
                print(self.map)
                tmp.next = None
                node.next = self.root
                self.root = node
                self.map[key] = value

    def log(self):
        node = self.root
        while node:
            print(node.val, end='->')
            node = node.next
        print()
        print('capcacity', self.cap)



test_case = [[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]], [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]]


def test_it(test_case):
    cache = LRUCache(test_case[0][0])


    for todo in test_case:
        if len(todo) == 1:
            print(cache.get(todo[0]))
            cache.log()
        else:
            cache.put(todo[0],todo[1])
            cache.log()

for i in test_case:
    test_it(i)
