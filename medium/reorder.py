class Node:
    def __init__(self, val: int = 0,next=None):
        self.val = val
        self.next = next

def reorderList(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head:
        return head
    arr = []
    idx = 0
    while head:
        arr.append(head)
        head = head.next
    root = None
    while idx < len(arr) and arr[idx] != arr[-1]:
        if root == None:
            root = arr[idx]
            head = root
            root.next = arr.pop()
            root = root.next
        else:
            root.next = arr[idx]
            root = root.next
            root.next = arr.pop()
            root = root.next
        idx+=1
    if idx < len(arr) and arr[idx] == arr[-1]:
        root.next = arr.pop()
        root = root.next
    root.next = None

print()
head = None
root = None
for i in range(1,5):
    tmp = Node(i)
    if head == None:
        root = tmp
        head = root
    else:
        root.next = tmp
        root = root.next

reorderList(head)

while head:
    print(head.val)
    head = head.next

print()
for i in range(1,6):
    tmp = Node(i)
    if head == None:
        root = tmp
        head = root
    else:
        root.next = tmp
        root = root.next

reorderList(head)

while head:
    print(head.val)
    head = head.next


print()
head = None
root = None
for i in range(1,10):
    tmp = Node(i)
    if head == None:
        root = tmp
        head = root
    else:
        root.next = tmp
        root = root.next

reorderList(head)

while head:
    print(head.val)
    head = head.next


for i in range(1,6):
    tmp = Node(i)
    if head == None:
        root = tmp
        head = root
    else:
        root.next = tmp
        root = root.next

reorderList(head)

while head:
    print(head.val)
    head = head.next

