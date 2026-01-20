test_case = [[1,2,3,7,8,9,4,5,6], [1,2,3,4,5,6], [1,1,1,1,1,2,2,2,3,3,3,5], [-1,-2,-5,10,11],[0,0,-1]]

def insertion_sort(arr):
    l = len(arr)
    for i in range(l):
        key = arr[i]
        j = i-1
        while 0 <= j and arr[j] >= key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

'''
for t in test_case:
    print(insertion_sort(t))
'''

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def print_nodes(node):
    while node:
        print(node.val,end='->')
        node = node.next
    return 

def insertion_sort_linked_list(head):
    if not head:
        return head
    sorted_l = None
    while head:
        next = head.next
        if not sorted_l or sorted_l.val <= head.val:
            head.next = sorted_l
            sorted_l = head
        else:
            tmp = sorted_l
            while tmp.next and tmp.next.val >= head.val:
                tmp = tmp.next
            head.next = tmp.next
            tmp.next = head
        head = next
    return sorted_l


for t in test_case:
    node = None
    head = None
    for n in t:
        if not node:
            node = Node(n)
            head = node
        else:
            head.next = Node(n)
            head = head.next
    new_node = insertion_sort_linked_list(node)
    print_nodes(new_node)
    print()

