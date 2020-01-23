from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        countChars = {}
        for characters in char:
            
        for word in words: 
            word = Counter(chars)
            wordKeys = word.keys()
        for key,value in countChars:
            if key in value:
                count += len(key)
        return count