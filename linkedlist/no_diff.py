class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

a = Node(1)
a.next = Node(0)
class t:
    def __init__(self,val):
        self.val = val
        self.next = None

x = t(1)
x.next = t(0)
print(a.val,a.next.val)
print(x.val,x.next.val)
