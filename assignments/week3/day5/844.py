#https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def compress(A):
            stack = list()
            for c in A:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop() 
            return stack
        
        return compress(S) == compress(T)
    
