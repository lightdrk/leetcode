#inorder traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def add(self, root, node):
        temp = root
        while temp:
            if temp.val > node.val:
                if not temp.left:
                    temp.left = node
                    break
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = node
                    break
                temp = temp.right

    def inorder(self, root):
        output = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            print(stack)
            top = stack.pop()
            output.append(top.val)
            curr = top.right

        return output


root = TreeNode(15)
print(root.val, root.left, root.right)
for i in [1,2,13,12,17,16,19]:
    temp = TreeNode(i)
    root.add(root, temp)

print(root.inorder(root))
