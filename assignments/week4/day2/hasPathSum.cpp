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
    bool hasPathSum(TreeNode* root, int sum) {
        // decrement the sum
        if(root == nullptr){
            return false;
        }
        int n_sum = sum - root->val;
        if(root->left == nullptr && root->right == nullptr){
            return (n_sum==0);
        }
        return hasPathSum(root->left,n_sum) || hasPathSum(root->right,n_sum);
    }
};

// https://leetcode.com/problems/path-sum/