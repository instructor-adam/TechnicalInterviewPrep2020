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
    int rangeSumBST(TreeNode* root, int L, int R) {
        int sum = 0;
        queue<TreeNode*> nodes;
        nodes.push(root);
        while(!nodes.empty()){
            auto node = nodes.front();
            nodes.pop();
            if((node->val>=L) && (node->val<=R)){
                sum += node->val;
            }
            if(node->left!=nullptr){
                nodes.push(node->left);
            }
            if(node->right!=nullptr){
                nodes.push(node->right);
            }
        }
        return sum;
    }
};