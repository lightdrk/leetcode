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


print("****************printing using recursion **************")
root = None
for n in [5,3,6,7,1,9]:
    root = binTree(root, n)
printing(root)

print("**************printing using iteration*****************")
root = None
for n in [5,3,6,7,1,9]:
    root = binary(root,n)
printingI(root)
