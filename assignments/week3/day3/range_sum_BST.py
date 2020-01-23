def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    range_obj = range(L, R + 1)
    sum = 0

    if root == None:
        return 0

    if root.val in range_obj:
        sum += root.val

    if root.right == None:
        return sum + self.rangeSumBST(root.left, L, R)
    if root.left == None:
        return sum + self.rangeSumBST(root.right, L, R)

    return sum + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(
        root.right, L, R)
