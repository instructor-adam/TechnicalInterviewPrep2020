class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        array = []
        sum = 0
        depth = 0
        max_depth = 0
        self.deepestLS(root, depth, array)
        for pair in array:
            if pair[1] > max_depth:
                max_depth = pair[1]

        for pair in array:
            if pair[1] == max_depth:
                sum += pair[0]
        return sum

    def deepestLS(self, root: TreeNode, depth: int, array: list):
        if root == None:
            return
        if root and root.left == None and root.right == None:
            array.append((root.val, depth))

        self.deepestLS(root.left, depth + 1, array)
        self.deepestLS(root.right, depth + 1, array)
