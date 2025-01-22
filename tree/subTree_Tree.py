class Tree:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubRoot(root,root2):
    def traverse(r1,r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return (r1.val == r2.val) and traverse(r1.left,r2.left) and traverse(r1.right,r2.right)
    stack = [root]
    while stack:
        tmp = stack.pop()
        if tmp.val == root2.val:
            if traverse(tmp,root2):
                return True
        if tmp.left:
            stack.append(tmp.left)
        if tmp.right:
            stack.append(tmp.right)
    return False

a = Tree(1)
b= Tree(1)
print(a==b)
