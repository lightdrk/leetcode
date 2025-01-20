class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def log(self):
        tmp = self
        while tmp:
            print(tmp.val,end='->')
            tmp = tmp.next
        print()

def add(l1,l2):
    val = 0
    carry = 0
    head = None
    root = ListNode()
    while l1 or l2 or carry:
        if l1:
            val+=l1.val
            l1 = l1.next
        if l2:
            val+=l2.val
            l2 = l2.next
        val+=carry
        carry = val//10
        val%=10
        if not head:
            root = ListNode(val)
            head = root
        else:
            root.next = ListNode(val)
            root = root.next
        val = 0

    return head

l1 = None
l2 = None
tmp = None
tmp2 = None
for i in range(5,10):
    if not l1:
        tmp = ListNode(i)
        l1 = tmp
    else:
        tmp.next = ListNode(i)
        tmp = tmp.next

for i in range(5,10):
    if not l2:
        tmp2 = ListNode(i)
        l2 = tmp2
    else:
        tmp2.next = ListNode(i)
        tmp2 = tmp2.next
l1.log()
l2.log()

x = add(l1,l2)
x.log()
