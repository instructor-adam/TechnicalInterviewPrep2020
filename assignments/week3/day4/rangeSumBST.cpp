/**
https://leetcode.com/problems/range-sum-of-bst/submissions/

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
    
    // depth-First Search
    int rangeSumBST(TreeNode* root, int L, int R) {
        if(root == NULL){
            return 0;
        }
        
        if(root->val < L){
            return rangeSumBST(root->right, L, R);
        }
        if(root->val > R){
            return rangeSumBST(root->left, L, R);
        }
        
        return root->val + rangeSumBST(root->right, L, R) + rangeSumBST(root->left, L, R);
        
//         queue<TreeNode*> nodes;
//         nodes.push(root);
//         int total = 0;
//         while (!nodes.empty()) {
//             auto node = nodes.front();
//             nodes.pop();
//             // cout << node->val << endl;
//             if ( node->left != nullptr) {
//                 if(node->val >= L && node->val <= R &&){
                    
//                 }
//                 cout << "*" << node->val << endl;
//                 total += node->val;
//                 nodes.push(node->left);    
//             }
            
//             if ( node->right != nullptr) {
//                 cout <<  "^" << node->val << endl;   
//                 total += node->val;
//                 nodes.push(node->right);
//             }
//         }
//         return total;
    }
};
