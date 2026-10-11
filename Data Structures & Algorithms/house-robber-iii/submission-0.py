# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            rob_node = node.val + left_skip + right_skip
            skip_node = max(left_rob, left_skip) + \
                        max(right_rob, right_skip)
            return (rob_node, skip_node)
        return max(dfs(root))