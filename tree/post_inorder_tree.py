class TreeNode:
    def __init__(self,val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left
def build(inorder,postorder):
    li = len(inorder)-1
    lp = len(postorder)
    root = TreeNode(postorder[-1])
    stack = [root]
    for i in range(lp-2,-1,-1):
        curr_node = TreeNode(postorder[i])
        if stack[-1].val != inorder[li]:
            stack[-1].right = curr_node
        else:
            parent = None
            while stack and stack[-1].val == inorder[li]:
                parent = stack.pop()
                li-=1
            parent.left = curr_node
        stack.append(curr_node)
    return root

def traversal(root):
    stack = [root]
    while stack:
        root = stack.pop()
        print(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


root = build([9,3,15,20,7],[9,15,7,20,3])
traversal(root)

