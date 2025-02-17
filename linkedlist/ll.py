class Node:
    def __init__(self, val :int,next=None):
        self.val = val
        self.next = next


root = None
t = None
for i in range(3):
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

def test(n,root):
    tmp = root
    tmp_root = None
    while tmp.next and tmp.next.val != n:
        tmp = tmp.next

    tmp_root = tmp.next
    tmp.next = tmp.next.next
    tmp_root.next = root
    root = tmp_root

    log(root)

test(3,root)
