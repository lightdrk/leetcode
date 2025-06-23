from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary(root, num):
    if not root:
        return TreeNode(num)
    curr = root
    while curr:
        if curr.val > num:
            if not curr.left:
                curr.left = TreeNode(num)
                break
            curr = curr.left

        elif curr.val < num:
            if not curr.right:
                curr.right = TreeNode(num)
                break
            curr = curr.right
    return root

def printingI(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val,"->",end=' ')
        root = root.right



def binTree(root, nums):
    if not root:
        return TreeNode(nums)

    if root.val > nums:
        root.left = binTree(root.left, nums)
    elif nums and root.val < nums:
        root.right = binTree(root.right, nums)
    return root

def printing(root):
    ''' inorder traversal '''
    if not root:
        return
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val,'->',end=' ')
        root = root.right
    return

def _inorder(root):
    if not root:
        return

    _inorder(root.left)
    print(root.val,end="->")
    _inorder(root.right)

def postorder(root):
    if not root:
        return
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        print(root.val, end='->')
        root = root.right
    return

def _postorder(root):
    if not root:
        return
    _postorder(root.left)
    _postorder(root.right)
    print(root.val)


def level(root):
    que = deque([root])
    output = []
    while que:
        length = len(que)
        out = []
        while length:
            root = que.popleft()
            out.append(root.val)
            if root.left:
                que.append(root.left)
            if root.right:
                que.append(root.right)
            length-=1
        output.append(out)

    for a in output:
        print(a)

def preorder(root):
    que = deque()
    while que or root:
        while root:
            print(root.val, end='->')
            que.append(root)
            root = root.left
        root = que.pop()
        root = root.right


def preorder_v2(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end='->')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


print("****************printing using recursion **************")
root = None
for n in [5,3,6,7,1,9]:
    root = binTree(root, n)
printing(root)
print()
print("**************printing using iteration*****************")
root = None
for n in [10,5,3,6,7,1,9,12,13,15,4]:
    root = binary(root,n)
printingI(root)
print()
print('************* recursion *******************')
_inorder(root)
print()

print('************* postorder *******************')
postorder(root)
print()

print('************* Recursion postorder *******************')
postorder(root)
print()

print('************* Recursion level order *******************')
level(root)
print()


print('************* Recursion preorder *******************')
preorder(root)
print()

print('************* Recursion preorder *******************')
preorder_v2(root)
print()

def delete(root,val):
    #BST

    def dell(root):
        if not root.left and not root.right:
            return
        if not root.left and root.right:
            return root.right
        if not root.right and root.left:
            return root.left
        if root.left and root.right:
            node = root
            prev = None
            while node:
                if not node.left and not node.left.left:
                    prev = node
                node = node.left
            root.val = node.val
            node.left = None

    if not root:
        return 
    # if node is leaf just remove
    # if node has one child replace it with him
    # if node has two child find successecor inorder or predecessor

    if root.val == val:
        dell(root)
        return

    while root:
        if root.val > val:
            if root.left.val == val:
                r = dell(root.left)
                if r:
                    root.left = r
                return
            root = root.left

        else:
            if root.right.val == val:
                r = dell(root.right)
                if r:
                    root.right = r
                return
            root = root.right
    return


delete(root,10)

print('************* recursion *******************')
_inorder(root)
print()
