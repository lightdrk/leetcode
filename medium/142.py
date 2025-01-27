class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def cycle(link):
    fast = link
    slow = link
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow.val
    return None

root = None
head = None

for i in range(10):
    tmp = Node(i)
    if root == None:
        head = tmp
        root = head
    else:
        head.next = tmp
        head = head.next

print(cycle(root))
