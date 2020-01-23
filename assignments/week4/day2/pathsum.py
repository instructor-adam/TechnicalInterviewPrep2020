def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root == None:
        return False

    sum = sum - root.val

    if root.right == None and root.left == None and sum == 0:
        return True

    if self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum):
        return True
    else:
        return False