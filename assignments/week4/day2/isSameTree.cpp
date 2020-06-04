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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // if one is null and the other isn't
        if(!p || !q){
        	if(q || p){
        		return false;
        	}
        }
        // if both nullptr
        if(p == nullptr && q == nullptr){
            return true;
        }
        // if values not same
        if(p->val != q->val){
            return false;
        }
        // else traverse trees
        if(isSameTree(p->left,q->left)&&isSameTree(p->right,q->right)){
        	return true;
        }
        return false;
    }
};