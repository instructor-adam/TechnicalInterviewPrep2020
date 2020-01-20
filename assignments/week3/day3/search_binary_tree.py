def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    if root == None or root.val == val:
        return root

    elif val > root.val:
        return self.searchBST(root.right, val)
    elif val < root.val:
        return self.searchBST(root.left, val)