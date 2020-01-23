class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.trav(p, q)

    def trav(self, p, q):
        # Termination condition for the Null nodes
        if not p and not q:
            return True

        if (not p and q) or (not q and p):
            return False

        # Termination condition
        if p.val != q.val:
            return False

        cond1 = self.trav(p.left, q.left)
        cond2 = self.trav(p.right, q.right)

        return True if cond1 and cond2 else False