/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Both are null
        if (p == nullptr && q == nullptr) {
            return true;
        }

        // One is null, other isn't
        if (p == nullptr || q == nullptr) {
            return false;
        }

        // Values are different
        if (p->val != q->val) {
            return false;
        }

        // Compare left and right subtrees
        return isSameTree(p->left, q->left) &&
               isSameTree(p->right, q->right);
    }
};
