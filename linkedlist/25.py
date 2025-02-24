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

def reverse(root,k):
    if k == 1 or not root.next or not root:
        return (root, root.next)
    node,node_next = reverse(root.next, k-1)
    root.next.next = root
    root.next = node_next
    return (node, node_next)

root = Node(0)
tmp = root
for n in range(1,6):
    tmp.next = Node(n)
    tmp = tmp.next

log(root)
print()

new, root.next = reverse(root, 3)
reverse(root,3)
log(new)
print()


