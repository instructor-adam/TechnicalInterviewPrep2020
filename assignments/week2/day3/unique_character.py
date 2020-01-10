def firstUniqChar(self, s: str) -> int:
    # traverse the string and store the index and the character as a tuple, with the frequency of
    # it

    # Traverse the dictionary and find the key that has value 1 and return that index

    # store char and index
    hash = {}

    for char_index in range(len(s)):
        if s[char_index] not in hash:
            hash[s[char_index]] = [1, char_index]
        else:
            hash[s[char_index]][0] += 1
    for value in hash.values():
        if value[0] == 1:
            return value[1]
    return -1
