#Brute Force
print('Brute Force')
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
    root = lists[0]
    for node in lists[1:]:
        root = combine(root,node)

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
