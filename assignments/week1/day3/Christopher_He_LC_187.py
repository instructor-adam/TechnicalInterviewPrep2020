from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lo = 0
        hi = 9
        d = defaultdict(int)
        while hi < len(s):
            d[s[lo:hi+1]] += 1
            lo += 1
            hi += 1
        
        return [k for k,v in d.items() if v > 1]
