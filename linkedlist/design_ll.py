class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.root = None

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        tmp = self.root
        while index > 0:
            index-=1
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.root
        self.root = node
        self.length+=1

    def addAtTail(self, val: int) -> None:
        self.length+=1
        node  = Node(val)
        if not self.root:
            self.root = node
        else:
            tmp = self.root
            while tmp.next:
                tmp = tmp.next
            tmp.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if self.length < index or index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            tmp = self.root
            while index > 1:
                index-=1
                tmp = tmp.next
            node = Node(val)
            node.next = tmp.next
            tmp.next = node
            self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        if 0 > index >= self.length:
            return
        if index == 0:
            self.root = self.root.next
        else:
            tmp = self.root
            while index > 1:
                index-=1
                tmp = tmp.next
            tmp.next = tmp.next.next
        self.length-=1

    def log(self):
        tmp = self.root
        print()
        print(self.length)
        print()
        while tmp:
            print(tmp.val,end='->')
            tmp = tmp.next
        print()

a = MyLinkedList()
a.addAtHead(5)
a.log()
a.addAtIndex(1,2)
a.log()
print(a.get(1))
a.addAtHead(6)
a.log()
a.addAtTail(2)
a.log()
print(a.get(3))
a.addAtTail(1)
print(a.get(5))
a.log()
a.addAtHead(2)
a.log()

print(a.get(2))

a.addAtHead(6)
a.log()
a.addAtIndex(5,0)
a.log()
a.addAtHead(6)

