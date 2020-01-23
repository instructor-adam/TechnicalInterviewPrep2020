def levelOrder(self, root: TreeNode) -> List[List[int]]:
    depth = 0
    hash = {}

    self.BFSTraversal(root, hash, depth)
    return hash.values()


def BFSTraversal(self, root: TreeNode, hash: dict, depth: int):
    if root == None:
        return

    if depth not in hash:
        hash[depth] = [root.val]
    else:
        hash[depth].append(root.val)

    self.BFSTraversal(root.left, hash, depth + 1)
    self.BFSTraversal(root.right, hash, depth + 1)