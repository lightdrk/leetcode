class Tree:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter(t):
    st = [(t,0)]
    far_dist = 0
    while st:
        root,dia = st.pop()
        if root.left:
            st.append((root.left, dia+1))
        if root.right:
            st.append((root.right, dia+1))
        far_dist = max(far_dist, dia)




