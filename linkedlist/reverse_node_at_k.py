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

head = Node(1)
tmp = head
for n in range(2,6):
    tmp.next = Node(n)
    tmp = tmp.next

k = 3
new, end = reverse(head, k)
tmp = head.next

while head and head.next:
    head.next, _ = reverse(head.next,k)
    head = tmp
    tmp = head.next
log(new)
#root.next, end = reverse(root.next,3)
#print()
#log(new)
#root = tmp
#tmp = root.next
#root.next, end = reverse(root.next,3)
#print()
#log(new)
