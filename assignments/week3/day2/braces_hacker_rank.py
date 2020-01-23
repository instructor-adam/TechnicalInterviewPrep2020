def braces(values):
    matched = []
    curly = "{}"
    square = "[]"
    braces = "()"

    for string in values:
        stack = []
        for char in string:
            if not stack:
                stack.append(char)

            elif char in curly:
                if char == stack[-1]:
                    stack.append(char)
                elif char != stack[-1] and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(char)
            elif char in square:
                if char == stack[-1]:
                    stack.append(char)
                elif char != stack[-1] and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(char)
            elif char in braces:
                if char == stack[-1]:
                    stack.append(char)
                elif char != stack[-1] and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            matched.append("YES")
        else:
            matched.append("NO")
    return matched
