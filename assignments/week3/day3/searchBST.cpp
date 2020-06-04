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
        queue<TreeNode*> nodes;
        nodes.push(root);
        while(!nodes.empty()){
            auto node = nodes.front();
            nodes.pop();
            if(node->val == val){
                return node;
            }
            if(node->left != nullptr){
                nodes.push(node->left);
            }
            if(node->right != nullptr){
                nodes.push(node->right);
            }
        }
        return nullptr;
    }
};