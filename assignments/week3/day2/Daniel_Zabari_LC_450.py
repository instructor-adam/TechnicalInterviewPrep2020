# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if (root is None):
            return root
        if (root.right is None) and (root.left is None):
            if root.val == key:
                return None
            return root
        prev = None
        current = root
        while current is not None:
            if key < current.val:
                prev = current
                current = current.left
            elif key > current.val:
                prev = current
                current = current.right
            elif key == current.val:
                break
        else:
            return root
        if (current.left is None) and (current.right is None):
            if prev is None:
                return None
            if prev.left == current:
                prev.left = None
            else:
                prev.right = None
            return root
        elif (current.left is None):
            if prev is None:
                return current.right
            if prev.left == current:
                prev.left = current.right
            else:
                prev.right = current.right
        elif (current.right is None):
            if prev is None:
                return current.left
            if prev.left == current:
                prev.left = current.left
            else:
                prev.right = current.left
        elif prev is None:
            root = current.right
            temp = current.left
            current = current.right
            while current is not None:
                prev = current
                current = current.left
            prev.left = temp
        elif prev.left == current:
            prev.left = current.right
            temp = current.left
            current = current.right
            while current is not None:
                prev = current
                current = current.left
            prev.left = temp
        elif prev.right == current:
            prev.right = current.left
            temp = current.right
            current = current.left
            while current is not None:
                prev = current
                current = current.right
            prev.right = temp
        return root

