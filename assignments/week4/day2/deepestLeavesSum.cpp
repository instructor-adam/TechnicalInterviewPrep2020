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
    int deepestLeavesSum(TreeNode* root){
        //deepest nodes are either in the left tree, right tree, or both
        // if one is deeper, take the deepestLeavesSum(deepest)
        // if @ same depth, take deepestLeavesSum of both, add them
        // in both cases, +1 to depth of the leaves to get depth relataive to original tree
        int sum_ = 0;
        sum_ = sum_ + root->val;
        // if root is the greatest depth
        if(root->left==nullptr && root->right==nullptr){
            return sum_;
        }

        int depth_ = 0;
        // return sum in the second value
        return get<1>(findSum(root,depth_l,depth_r));
    }
    // <depth, sum>
    pair<int,int> findSum(TreeNode* root){
        
    }
};

