print('v_2 LRU CACHE')

class Node:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self,cap):
        self.cap = cap
        self.root = None
        self.end = None
        self.map = {}

    def get(self, key):
        if not key in self.map:
            return -1
        print(self.cap)
        self.root.prev = self.map[key]
        self.map[key].prev.next = self.map[key].next
        self.map[key].prev = None
        self.map[key].next = self.root
        self.root = self.map[key]
        return self.root.val


    def put(self, key, value):
        if key not in self.map and self.cap:
            self.map[key] = Node(value,key)
            if not self.root:
                self.root = self.map[key]
                self.prev = self.root
                return
            else:
                self.map[key].next, self.root.prev = self.root, self.map[key]
                self.root = self.map[key]
                self.cap-=1
            return
        if key not in self.map and not self.cap:
            self.map[key] = Node(value,key)
            self.map[key].next = self.root
            print(self.prev.val, self.prev.key)
            self.map.pop(self.prev.key)
            print(self.map)
            self.root.prev = self.map[key]
            self.root = self.map[key]
            self.prev = self.prev.prev
            self.prev.next = None
            return

        if key in self.map:
            #update
            self.map[key].val = value
            self.map[key].prev = self.map[key].next
            self.map[key].next, self.root.prev = self.root, self.map[key]
            self.map[key].prev = None
            self.root = self.map[key]
            return

test = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

def testing(test):
    cache = LRUCache(test[0][0])
    for i in test[1:]:
        if len(i) == 1:
            print(cache.get(i[0]))
        else:
            cache.put(i[0],i[1])

testing(test)

