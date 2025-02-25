def reverse(root,k):
    if k == 1 and root:
        return (root, root.next)
    elif k >= 1 or not root:
        return (None, None)
    node, node_next = reverse(root.next, k-1)
    if not node:
        return (None, None)
    root.next.next = root
    root.next = node_next
    return (node, node_next)


class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next
def log(root):
    if not root:
        return
    while root:
        print(root.val, end='->')
        root = root.next

head = Node(1)
tmp = head
for n in range(2):
    tmp.next = Node(n)
    tmp = tmp.next
k = 2
new, _ = reverse(head,k)
log(new)
