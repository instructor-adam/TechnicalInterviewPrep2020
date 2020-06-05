class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        current_len = 0
        start_index = 0
        substring_dict = {}
        for index, char in enumerate(s):
            if char in substring_dict:
                if substring_dict[char] >= start_index:
                    start_index = substring_dict[char] + 1
                    current_len = index - start_index
            substring_dict[char] = index
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        return max_len
