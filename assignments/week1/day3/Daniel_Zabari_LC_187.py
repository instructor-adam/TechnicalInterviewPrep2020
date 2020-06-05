class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        j = i + 10
        length = len(s)
        seq = {}
        while j <= length:
            if s[i:j] in seq:
                seq[s[i:j]] += 1
            else:
                seq[s[i:j]] = 1
            i += 1
            j += 1
        repeated = []
        for key, value in seq.items():
            if value > 1:
                repeated.append(key)
        return repeated
