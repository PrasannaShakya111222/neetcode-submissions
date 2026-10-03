# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are empty
        if not p and not q:
            return True
        # One is empty, other isn't
        if not p or not q:
            return False
        # Values are different
        if p.val != q.val:
            return False
        # Check both subtrees
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )