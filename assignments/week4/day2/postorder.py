class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        arr = []
        self.dfs(root,arr)
        return arr
    
    def dfs(self, root, arr):
        if root.left:
            self.dfs(root.left,arr)
        if root.right:
            self.dfs(root.right,arr)
        
        arr.append(root.val)