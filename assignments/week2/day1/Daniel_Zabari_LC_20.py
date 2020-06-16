class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        for char in s:
            if char in "({[":
                paren_stack.append(char)
            elif paren_stack == []:
                return False
            elif char == ")":
                if paren_stack.pop() != "(":
                    return False
            elif char == "}":
                if paren_stack.pop() != "{":
                    return False
            elif char == "]":
                if paren_stack.pop() != "[":
                    return False
        return len(paren_stack) == 0
