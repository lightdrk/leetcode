
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
for n in range(2,8):
    tmp.next = Node(n)
    tmp = tmp.next

def reverse(root,k):
    if not root:
        return root
    arr = []
    count = 0
    while root:
        arr.append(root)
        root = root.next
        count+=1
    root = None
    count-=count%k
    print(count)
    while count:
        prev = arr[0]
        tmp = arr.pop(0)
        kk = k-1
        while kk:
            arr[0].next = tmp
            tmp.next = None
            tmp = arr.pop(0)
            kk-=1
        if not root:
            root = tmp
        prev.next = arr[0]
        count-=1
    return root

t = reverse(head, 2)
log(t)
