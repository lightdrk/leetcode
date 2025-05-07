from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maximumDepth(root):
    if not root:
        return 0
    #level order traversal
    #bfs
    que = deque([root])
    depth = 0
    while que:
        lvl = len(que)

        while lvl:
            if root.left:
                que.append(root.left)
            if root.right:
                que.append(root.right)
            lvl-=1

        depth+=1

    return depth


