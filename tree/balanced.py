class Tree:
    def __init__(self, val, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def balanced():
    if not root:
        return True
    def depth(root):
        if not root:
            return 0
        d = 0
        st = [(root,1)]
        while st:
            root, depth = st.pop()
            if root.left:
                st.append((root.left,depth+1))
                if root.right:
                    st.append((root.right,depth+1))
                if d < depth:
                    d = depth
        print(depth)
        return d
    return abs(depth(root.left)- depth(root.right)) > 1


