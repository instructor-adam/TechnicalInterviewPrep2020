/* https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/ */

TreeNode* searchBST(TreeNode* root, int val) {
    if(root->val == val){
        return root;
    }else if (val < root->val && root->left != NULL){
        return searchBST(root->left, val);
    }else if(val > root->val && root->right != NULL){
        return searchBST(root->right, val);
    }else{
        return NULL;
    }
}
