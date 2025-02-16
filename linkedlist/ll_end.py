class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


root = None
tmp = None
for i in range(1):
    node = Node(i)
    if not root:
        root = node
        tmp = root
    else:
        tmp.next = node
        tmp = tmp.next

while root.next and root.next.next:
    print(root.val,end='->')
    root = root.next

print()
print('root.next', root.next.val)
print(root.next.next)
