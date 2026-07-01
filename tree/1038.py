
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def Tree(val: int,toor: TreeNode|None):
    if not toor:
        return TreeNode(val)
    root = toor
    while root:
        if root.val > val:
            if not root.left:
                root.left = TreeNode(val)
                break
            root = root.left
        else:
            if not root.right:
                root.right = TreeNode(val)
                break
            root = root.right
    return toor


test_case = [[1,2,3,4,5,6,7,8],[5,6,3,2,1,8,9]]

'''
def convertToGreaterTree(root :TreeNode|None):
    def inorder(root):
        if not root:
            return
        inorder(root.right)
        if root.right:
            print(root.val+root.right.val,end="->")
        else:
            print(root.val,end="->")
        inorder(root.left)
    inorder(root)
'''
order = [0]
def convert(root):
    if not root:
        return
    convert(root.right)
    root.val+=order[0]
    order[0] = root.val
    print(root.val,end='->')
    convert(root.left)



for t in test_case:
    root = None
    for i in t:
        root = Tree(i,root)
    print("printing the tree --->")
    convert(root)
