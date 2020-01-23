def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1

    if t1 and t2:
        t1.val += t2.val

    if t1.left and t2.left:
        self.mergeTrees(t1.left, t2.left)

    if t1.right and t2.right:
        self.mergeTrees(t1.right, t2.right)

    if not t1.right and t2.right:
        t1.right = t2.right
    if not t1.left and t2.left:
        t1.left = t2.left

    return t1