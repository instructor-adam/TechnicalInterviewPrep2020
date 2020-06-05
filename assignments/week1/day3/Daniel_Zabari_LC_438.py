class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s == "":
            return []
        if len(p) > len(s):
            return []
        anagram = {}
        for char in p:
            if char not in anagram:
                anagram[char] = 0
            anagram[char] += 1
        i = 0
        j = len(p) - 1
        length = len(s)
        index_list = []
        sub_dict = {}
        for char in s[:j+1]:
            if char not in sub_dict:
                sub_dict[char] = 0
            sub_dict[char] += 1
        if sub_dict == anagram:
            index_list.append(i)
        while (j + 1) < length:
            sub_dict[s[i]] -= 1
            if sub_dict[s[i]] == 0:
                del sub_dict[s[i]]
            i += 1
            j += 1
            if s[j] not in sub_dict:
                sub_dict[s[j]] = 0
            sub_dict[s[j]] += 1
            if sub_dict == anagram:
                index_list.append(i)
        return index_list
