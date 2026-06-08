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



def mergeLL_v1(lists):
    def merge_sort(arr,l)-> (Node|None):
        print(l)
        if l == 1:
            return arr[-1]
        if l <= 0:
            return None

        half = l//2
        left = merge_sort(arr[:half],half)
        right = merge_sort(arr[half:],l-half)


        if not left:
            return right
        if not right:
            return left

        temp = root = Node(-1)
        while left and right:
            print(left.val,right.val)
            if left.val > right.val:
                temp.next = Node(right.val)
                right = right.next
            else:
                temp.next = Node(left.val)
                left = left.next
            temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return root.next
    root = merge_sort(lists,len(lists))
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

root = mergeLL_v1(lists)
log(root)

test = [[],[],[]]
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

root = mergeLL_v1(lists)
log(root)

