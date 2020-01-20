# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        queue.append(root)
        while(queue):
            count = len(queue)
            while(count>0):
                tree = []
                TreeNode = queue.pop(0)
                if TreeNode.left is not None:
                    queue.append(TreeNode.left)
                    tree.append(TreeNode.left.val)
                if TreeNode.right is not None:
                    queue.append(TreeNode.right)
                    tree.append(TreeNode.right.val)
                count -= 1
            print(tree, end=',')