from typing import Optional

class Node:
    def __init__(self, val :int = 0, left :Optional['Node'] = None , right :Optional['Node']= None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, val :int):
        self.root = Node(val)

    def binT(self, val:int = 0):
        node = self.root
        new = Node(val)
        while node:
            if node.val > val:
                if not node.left:
                    break
                node = node.left
            else:
                if not node.right:
                    break
                node = node.right
        if node.val > val:
            node.left = new
        else:
            node.right = new
        return

    def inorder_(self):
        node = self.root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node  = stack.pop()
            print(node.val, end="->")
            node = node.right

    def inorder(self):
        def recur(node):
            if not node:
                return
            recur(node.left)
            print(node.val,end='->')
            recur(node.right)

        return recur(self.root)

    def postorder(self):
        def recur(node):
            if not node:
                return
            recur(node.left)
            recur(node.right)
            print(node.val,end='->')
        return recur(self.root)
bT = Tree(6)
for i in range(10,-1,-1):
    bT.binT(i)

bT.inorder_()
print()
bT.inorder()
print()
print('<-- Post order Traversal ->')
bT.postorder()
