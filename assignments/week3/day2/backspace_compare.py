def backspaceCompare(self, S: str, T: str) -> bool:
    stack_S = []
    stack_T = []

    for char in S:
        if char == "#" and not stack_S:
            continue
        elif char == "#":
            stack_S.pop()
        else:
            stack_S.append(char)

    for char in T:
        if char == "#" and not stack_T:
            continue
        elif char == "#":
            stack_T.pop()
        else:
            stack_T.append(char)
    return True if stack_S == stack_T else False
