# https://leetcode.com/problems/unique-number-of-occurrences/submissions/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        arrCount = collections.Counter(arr)
        timesCount = collections.Counter(arrCount.values())
        
        for item in timesCount:
            if timesCount[item] > 1:
                return False
            
        return True
