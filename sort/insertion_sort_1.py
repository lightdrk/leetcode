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

def insertion_sort_reverse(arr):
    l = len(arr)
    for i in range(l):
        key = arr[i]
        j = i - 1
        while 0 <= j and arr[j] <= key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


def l_to_ll(arr):
    root = head = None
    for n in arr:
        if not root:
            root = Node(n)
            head = root
        else:
            head.next = Node(n)
            head = head.next
    return root

def printL(root):
    while root:
        print(root.val, end='->')
        root = root.next
    print()
    return 

def insertion_sort_linked_list(head):
    curr = head
    while curr:
        tmp = curr
        tmp_next = curr.next


for t in test_case:
    print(insertion_sort(t))
    print(insertion_sort_reverse(t))
    printL(l_to_ll(t))
