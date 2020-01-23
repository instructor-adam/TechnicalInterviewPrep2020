class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        self.dfs(root, target)
        if root.val == target and not root.left and not root.right:
            return None
        return root

    def dfs(self, root, target):
        if not root:
            return None

        root.left = self.dfs(root.left, target)
        root.right = self.dfs(root.right, target)

        if not root.left and not root.right and root.val == target:
            print("TEST")
            return None

        return root