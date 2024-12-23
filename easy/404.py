#sum of left leaves
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    #bfs
    s_m = 0
    que = [(root, False)]
    while que:
        (root, yes) = que.pop(0)
        if yes and root and not root.left and not root.right:
            s_m = s_m + root.val

            if root.left:
                que.append((root.left,True))

            if root.right:
                que.append((root.right, False))

        return s_m
