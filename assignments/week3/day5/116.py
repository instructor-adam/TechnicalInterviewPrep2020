# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        q = collections.deque([(root, 0)])
        while q:
            node,depth = q.popleft() 
            if not node:
                continue
            q.extend([(node.left, depth+1), (node.right, depth+1)]) 
            if depth == q[0][1]:
                node.next = q[0][0]
        return root
            