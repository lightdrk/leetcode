'''

You are a professional robber planning to rob houses along a binary tree. Each node in the tree represents a house with some amount of money.

The constraint is:

If you rob a house (i.e., a node), you cannot rob its immediate children (left or right child).

You may rob any subset of the houses, but no two directly-linked houses.

Return the maximum amount of money you can rob without alerting the police.



'''
from typing import Optional
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        exclude = self.rob(root.left) + self.rob(root.right)
        include = root.val
        if root.right:
            include+=self.rob(root.right.left)+self.rob(root.right.right)
        if root.left:
            include+=self.rob(root.left.right) + self.rob(root.left.left)

        return max(exclude,include)



