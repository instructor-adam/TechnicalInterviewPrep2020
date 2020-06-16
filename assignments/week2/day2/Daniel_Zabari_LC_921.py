class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        paren_stack = []
        count = 0
        for char in S:
            if char == "(":
                paren_stack.append(char)
            elif paren_stack == []:
                count += 1
            else:
                paren_stack.pop()
        return count + len(paren_stack)
