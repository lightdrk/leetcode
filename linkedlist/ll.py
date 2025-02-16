class Node:
    def __init__(self, val :int,next=None):
        self.val = val
        self.next = next


root = None
t = None
for i in range(7):
    tmp = Node(i)
    if not root:
        root = tmp
        t = root
    else:
        t.next = tmp
        t = t.next

def log(root):
    while root:
        print(root.val,end='->')
        root = root.next
    print()
    return



tmp = root
tmp_root = None
while tmp.next and tmp.next.val != 2:
    tmp = tmp.next

tmp_root = tmp.next
tmp.next = tmp.next.next
tmp_root.next = root
root = tmp_root

log(root)

tmp = root
tmp_root = None
while tmp.next and tmp.next.val != 5:
    tmp = tmp.next

tmp_root = tmp.next
tmp.next = tmp.next.next
tmp_root.next = root
root = tmp_root

log(root)

tmp = root
tmp_root = None
while tmp.next and tmp.next.val != 6:
    tmp = tmp.next

tmp_root = tmp.next
tmp.next = tmp.next.next
tmp_root.next = root
root = tmp_root

log(root)
