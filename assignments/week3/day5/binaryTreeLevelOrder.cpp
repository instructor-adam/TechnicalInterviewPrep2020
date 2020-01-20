/**
https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> level_order;
        vector<pair<int, int>> level_tracker;
        int depth = 1;
        queue<pair<TreeNode*, int>> nodes;
        
        nodes.push(make_pair(root, depth)); // root
        
        // cout << nodes.front().first->val << ", " << nodes.front().second << endl;
        
        while (!nodes.empty()) {
            auto node = nodes.front();

            cout << node.first->val <<", " << node.second << endl;
            
            if(node.first->left != nullptr || node.first->right != nullptr){
                depth++;
            }

            if (node.first->left != nullptr) {
                level_tracker.push_back(make_pair(node.first->left->val, depth));
                nodes.push(make_pair(node.first->left, depth));
            }
            
            if (node.first->right != nullptr) {
                level_tracker.push_back(make_pair(node.first->right->val, depth));

                nodes.push(make_pair(node.first->right, depth));
            }     
            nodes.pop();
        }

        
        int curr_depth = 1;
        vector<int> temp;
        
        return level_order;
    }
    
};
