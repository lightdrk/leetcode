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
        print('getting ->', key)
        if not key in self.map:
            return -1
        if self.root == self.map[key]:
            return self.root.val
        if self.end == self.map[key]:
            self.end = self.end.prev
            print('updating end ->>>',self.end.key)
        self.root.prev = self.map[key]
        if self.map[key].prev:
            self.map[key].prev.next = self.map[key].next
        if self.map[key].next:
            self.map[key].next.prev = self.map[key].prev

        self.map[key].prev = None
        self.map[key].next = self.root
        self.root = self.map[key]
        return self.root.val


    def put(self, key, value):
       # if key not in self.map:
       #     if self.cap:
       #         self.map[key] = Node(value,key)
       #         if not self.root:
       #             self.root = self.map[key]
       #             self.end = self.root
       #         else:
       #             self.map[key].next, self.root.prev = self.root, self.map[key]
       #             self.root = self.map[key]
       #         self.cap-=1
       #         return
       #     else:
       #         print(self.end.val,self.end.key,self.end.prev,self.end.next)
       #         self.map[key] = Node(value,key)
       #         self.map[key].next = self.root
       #         self.map.pop(self.end.key)
       #         self.root.prev = self.map[key]
       #         self.root = self.map[key]
       #         self.end = self.end.prev
       #         self.end.next = None
       #         return

       # if key in self.map:
       #     #update
       #     self.map[key].val = value
       #     self.map[key].prev = self.map[key].next
       #     self.map[key].next, self.root.prev = self.root, self.map[key]
       #     self.map[key].prev = None
       #     self.root = self.map[key]
       #     return
        if not key in self.map:
            node = Node(value,key)
            if self.cap:
                self.map[key] = node
                if not self.root:
                    self.end = self.root = node
                else:
                    self.root.prev, node.next = node, self.root
                    self.root = node
                self.cap-=1
            else:
                #add new node to front
                self.root.prev, node.next = node, self.root
                self.root = node
                #pop from end
                self.map[key] = node
                self.map.pop(self.end.key)
                self.end = self.end.prev
                self.end.next = None

        else:
            #updated pointes
            if self.root != self.end:
                if self.end.prev:
                    self.end = self.end.prev
                if self.end.next:
                    self.end.next = None
                node = self.map[key]
                self.root.prev, node.next = node, self.root
                node.prev = None
                self.root = node
            self.root.val = value
        return

    def log(self):
        tmp = self.root
        print('end ->', self.end.key)
        while tmp:
            print(tmp.key,end='->')
            tmp = tmp.next
        print()

test = [[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]],[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]], [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]]

def testing(test):
    cache = LRUCache(test[0][0])
    for i in test[1:]:
        if len(i) == 1:
            print('0----------0')
            print(cache.get(i[0]))
            cache.log()
        else:
            print(f'--------put ({i})-------')
            cache.put(i[0],i[1])
            cache.log()
for t in test:
    print(t)
    testing(t)

