class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        array = []
        self.retainTree(root, array)
        return array

    def retainTree(self, root, array):
        if root == None:
            return
        else:
            array.append(root.val)

        self.retainTree(root.left, array)
        self.retainTree(root.right, array)
