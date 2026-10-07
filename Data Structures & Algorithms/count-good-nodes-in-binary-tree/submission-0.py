# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_value):
            if not node:
                return 0
            count = 0
            if node.val >= max_value:
                count = 1
                max_value = node.val
            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)
            return count
        return dfs(root, root.val)