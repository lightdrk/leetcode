class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


t = root = None
tmp = None
for i in range(4):
    node = Node(i)
    if not root:
        root = node
        tmp = root
    else:
        tmp.next = node
        tmp = tmp.next

while root.next:
    print(root.val,end='->')
    root = root.next

root.next = None

while t:
    print(t.val, end="->")
    t = t.next
