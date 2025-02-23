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
    if k == 0 or not root.next or not root:
        return root
    node = reverse(root.next, k-1)
    root.next.next = root
    root.next = None
    return node

root = Node(0)
tmp = root
for n in range(1,6):
    tmp.next = Node(n)
    tmp = tmp.next
new = reverse(root, 2)

log(root)
print()
log(new)


