# found this problem alittle confusing 
# had to look at solution 
# trees are difficult for me

def isSimilar(self, s1, s2):
    if s1 is None and s2 is None:
        return True 
    if s1 is None or s2 is None:
        return False 
    return s1.val == s2.val and self.isSimilar(s1.left, s2.right) and self.isSimilar(s1.right, s2.left)
    
def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True 
    return self.isSimilar(root.left, root.right )
    