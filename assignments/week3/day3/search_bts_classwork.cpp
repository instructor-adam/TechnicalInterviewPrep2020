/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        stack<TreeNode*> nodes;
        nodes.push(root);
        while (!nodes.empty()) {
            TreeNode* node = nodes.top();
            nodes.pop();
            if (node->val == val){
                return node;
            }
            if (node->right != nullptr) {
                nodes.push(node->right);

            }
            if (node->left != nullptr) {
                nodes.push(node->left);
            }
        }
        return nullptr;
    }
};