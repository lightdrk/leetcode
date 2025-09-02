'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level
'''


#follow up


'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between)
'''
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self,val: int=0,next: Optional[ListNode]=None):
        self.val = val
        self.next = next

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque([root])
        zig = False
        output = []
        while que:
            l = len(que)
            ans = []
            for _ in range(l):
                root = que.popleft()
                ans.append(root.val)
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)
            if zig:
                ans = ans[::-1]
            output.append(ans)
            zig = not zig
        return output

    def zigzagLevelOrderLinkedList(self, root: Optional[TreeNode]) -> List[Optional[ListNode]]:

        if not root:
            return []

        def helper(root):
            reverse = None

            while root:
                new  = root
                root = root.next
                new.next = reverse
                reverse = new
            return reverse 

        que = deque([root])
        zig = False
        output = []
        while que:
            l = len(que)
            head = None
            tail = None
            for _ in range(l):
                root = que.popleft()
                curr = ListNode(root.val)
                if not head:
                    head = curr
                    tail = head
                else:
                    tail.next = curr
                    tail = tail.next
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)
            if zig:
                head = helper(head)
            output.append(head)
            zig = not zig
        return output



def helper(root):
    reverse = None

    while root:
        new  = root
        root = root.next
        new.next = reverse
        reverse = new
    return reverse 



head = None
tail = None
l = 10
for val in range(l):
    curr = ListNode(val)
    if not head:
        head = curr
        tail = head
    else:
        tail.next = curr
        tail = tail.next

head = helper(head)
while head:
    print(head.val,end="->")
    head = head.next

