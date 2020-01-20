def connect(self, root: 'Node') -> 'Node':
    hash = {}
    depth = 0

    self.traversal(root, hash, depth)

    for level_nodes in hash.values():
        for index in range(len(level_nodes)):
            if index == len(level_nodes) - 1:
                break
            level_nodes[index].next = level_nodes[index + 1]
    return root


def traversal(self, root: TreeNode, hash: dict, depth: int):
    if root == None:
        return

    if depth not in hash:
        hash[depth] = [root]
    else:
        hash[depth].append(root)

    self.traversal(root.left, hash, depth + 1)
    self.traversal(root.right, hash, depth + 1)