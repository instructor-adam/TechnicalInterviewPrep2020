 #O(n) time, O(n) space 
 def wordPattern(pattern, str):
        lst = str.split(' ')
        if not len(pattern) is len(lst):
            return False 
        
        seen_char = {}
        seen_word = {}
        for i, j in zip(range(len(pattern)),range(len(lst))):
            if not pattern[i] in seen_char.keys() and not lst[i] in seen_word.keys():
                seen_char[pattern[i]] = lst[i]
                seen_word[lst[i]] = pattern[i]
            elif pattern[i] in seen_char.keys() and not lst[i] in seen_word.keys():
                return False
            elif not pattern[i] in seen_char.keys() and lst[i] in seen_word.keys():
                return False
            else:
                if not lst[i] == seen_char[pattern[i]] or not lst[i] == seen_char[pattern[i]]:
                    return False
                                                                          
        return True 