class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if (root is None):
            return True
        return self.symmetrees(root.left, root.right)

    def symmetrees(self, left: TreeNode, right: TreeNode)-> bool:
        if ((left is None) or (right is None)):
            return ((left is None) and (right is None))
        if (left.val != right.val):
            return False
        one_way = self.symmetrees(left.left, right.right)
        return (one_way and self.symmetrees(left.right, right.left))
