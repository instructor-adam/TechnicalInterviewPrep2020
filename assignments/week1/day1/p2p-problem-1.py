class Solution(object):
    def toLowerCase(self, s):
        """
        :type str: str
        :rtype: str
        """
        
        self.s = ''.join([ (chr(ord(c) + 32)*(ord(c) >= 65 and ord(c) <= 90)) or c for c in s ])
        return self.s
