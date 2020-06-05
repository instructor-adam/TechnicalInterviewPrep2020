from collections import defaultdict

class Solution:
    def findAnagrams(self, s, p):
        
        res = []
        if len(s) < len(p):
            return res
        
        d1 = defaultdict(int)
        for char in p:
            d1[char] += 1
        
        d2 = defaultdict(int)
        for i in range(len(p)):
            char = s[i]
            if char in d1:
                d2[char] += 1

        lo = 0
        hi = len(p)

        while hi < len(s):
            if d1 == d2:
                res.append(lo)

            char1 = s[lo]
            char2 = s[hi]

            if char1 in d1:
                d2[char1] -= 1

            if char2 in d1:
                d2[char2] += 1

            lo += 1
            hi += 1
        
        if d1 == d2:
            res.append(lo)
            
        return res
