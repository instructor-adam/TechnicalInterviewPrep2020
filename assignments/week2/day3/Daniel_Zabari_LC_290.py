class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split(' ')
        word_set = set()
        decode = {}
        if len(words) != len(pattern):
            return False
        for index, word in enumerate(words):
            if pattern[index] in decode:
                if decode[pattern[index]] != word:
                    return False
            elif word in word_set:
                return False
            else:
                decode[pattern[index]] = word
                word_set.add(word)
        return True
