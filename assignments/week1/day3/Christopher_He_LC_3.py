class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
            if len(s) < 2:
                return len(s)
            
            lo = 0
            d = {}
            d[s[0]] = 0
            length = 1
            
            for i in range(1,len(s)):
                char = s[i]
                if char in d and d[char] >= lo:
                    length = max(length, i - lo)
                    lo = d[char] + 1
                d[char] = i
            
            length = max(length, len(s) - lo)
            return length
