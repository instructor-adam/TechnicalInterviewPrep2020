# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sCount = collections.Counter(S)
        jSet = set(J)
        totGems = 0
        for item in sCount:
            if item in jSet:
                totGems += sCount[item]

        return totGems

# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        arrCount = collections.Counter(arr)
        timesCount = collections.Counter(arrCount.values())
        
        for item in timesCount:
            if timesCount[item] > 1:
                return False
            
        return True


# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        sList = string.split()
        mapping = dict()
        seen = set()
        if len(sList) != len(pattern):
            return False
        for c,word in zip(pattern, sList):
            if c not in mapping and word not in seen:
                seen.add(word)
                mapping[c] = word
            else:
                if c not in mapping or mapping[c] != word:
                   return False
        return True

