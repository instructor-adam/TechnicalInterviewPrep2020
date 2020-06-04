class Solution(object):
    def noRepStr(self, ss):
        seen = {}
        for i in range(len(ss)):
            if not ss[i] in seen.keys():
                seen[ss[i]] = True
            else:
                return 0 
        return len(ss)
    
    def lengthOfLongestSubstring(self, s):
        longest = 0 
        #generate all substrings 
        for i in range(len(s)):
            j = i + 1
            for j in range(len(s)+1):    
                #check if substr has repeating characters
                guess = self.noRepStr(s[i:j])
                #maintain longest substr
                if longest < guess:
                    longest = guess
        return longest 
#overall runtime O(N^3), 986 of 987 test cases passed. see image in folder 