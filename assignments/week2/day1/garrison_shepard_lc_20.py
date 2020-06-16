
def isValid(self, s):
    
    if len(s) == 0:
        return True

    if len(s) % 2:
        return False 

    stack = []
    match = ('()', '[]', '{}')
    stack.append(s[0])

    for i in range(1, len(s)):
        if len(stack) > 0 and (stack[-1] + s[i]) in match:
            stack.pop()
        else:
            stack.append(s[i])

    if not len(stack) == 0:
        return False

    return True 