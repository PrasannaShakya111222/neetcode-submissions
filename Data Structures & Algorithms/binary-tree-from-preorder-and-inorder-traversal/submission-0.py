# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0
        def build(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            # Get root from preorder
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            mid = index_map[root_val]
            # Build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(inorder) - 1)