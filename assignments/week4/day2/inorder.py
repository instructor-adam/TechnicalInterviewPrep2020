class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        arr = []
        self.dfs(root,arr)
        return arr
    
    def dfs(self, root, arr):
        if root.left:
            self.dfs(root.left,arr)
        arr.append(root.val)
        if root.right:
            self.dfs(root.right,arr)
        