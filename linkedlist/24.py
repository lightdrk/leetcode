class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def swap(head):
    if not head:
        return
    root = None
    prev = None
    while head:
        first = head
        second = head.next
        if not root:
            root = second
        if prev:
            prev.next = second
        first.next = second.next
        second.next = first
        prev = first
        head = first.next
    return root

head = Node(1)
tmp = head
for n in range(2,5):
    tmp.next = Node(n)
    tmp = tmp.next

root = swap(head)
while root:
    print(root.val)
    root = root.next
