# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
class Solution:
    def isHappy(self, n: int) -> bool:
        i = n
        loop = set()
        while i >= 1:
            if i == 1:
                return True
            elif i in loop:
                return False
            else:
                loop.add(i)
                i = sum([int(c)*int(c) for c in str(i)])
        
