print('#Optmize usage')

def log(root):
    while root:
        print(root.val,end='->')
        root = root.next
    print()


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeLL(lists):
    def combine(node1,node2):
        root = None
        tmp = None
        while node1 and node2:
            node = node1
            if node1.val >= node2.val:
                node = node2
                node2 = node2.next
            else:
                node1 = node1.next

            if not root:
                root = node
                tmp = root
            else:
                tmp.next = node
                tmp = tmp.next
        if node1:
            tmp.next = node1
        if node2:
            tmp.next = node2
        return root
    def merge(lists):
        length = len(lists)
        if length <= 1:
            return lists
        mid = length//2
        left = merge(lists[:mid])
        right = merge(lists[mid:])
        return [combine(left, right)]
    return root

test = [[1,4,5],[1,3,4],[2,6]]
lists = []
for i in range(len(test)):
    root = None
    tmp = None
    for n in test[i]:
        node = Node(n)
        if not root:
            root = node
            tmp = root
        else:
            tmp.next = node
            tmp = tmp.next
    lists.append(root)

root = mergeLL(lists)
log(root)

