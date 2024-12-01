class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addHead(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def addTail(self,val):
        node = Node(val)
        if not self.head:
            self.head = Node(val)
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        #this is not while tmp: because it goes to end meaning to None which make tmp not a node rather becomes simply a None value variable
        #so that is why we stop before becomming none
        tmp.next = node

    def _printIndex(self, index):
        tmp = self.head
        while tmp:
            if index == 1:
                print(tmp.val)
            tmp = tmp.next
            index = index - 1

    def _print(self):
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

x = LinkedList()

for i in range(1,10):
    x.addTail(i)
    x.addHead(i)

x._print()
x._printIndex(7)

