class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        max_length = 1
        start_index = 0
        end_index = 0
        pal_table = [[0 for _ in s] for _ in s]
        # Place single letters in tabulation:
        for i in range(len(s)):
            pal_table[i][i] = 1
        # Place double letters in tabulation:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                pal_table[i][i+1] = 2
                start_index = i
                end_index = i + 1
                max_length = 2
        diff = 2
        while diff < len(s):
            i = 0
            while i < (len(s) - diff):
                j = i + diff
                if (pal_table[i+1][j-1] > 0) and (s[i] == s[j]):
                    pal_table[i][j] = pal_table[i+1][j-1] + 2
                    if max_length < pal_table[i][j]:
                        max_length = pal_table[i][j]
                        start_index = i
                        end_index = j
                i += 1
            diff += 1
        return s[start_index:end_index+1]
