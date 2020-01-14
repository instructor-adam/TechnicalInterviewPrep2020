def braces(values):
    matched = []
    curly = "{}"
    square = "[]"
    braces = "()"

    for string in values:
        curly_stack = []
        square_stack = []
        braces_stack = []

        for char in string:
            if char in curly:
                if not curly_stack:
                    curly_stack.append(char)
                elif curly_stack[-1] == char:
                    curly_stack.append(char)
                elif curly_stack[-1] != char:
                    curly_stack.pop()

            elif char in square:
                if not square_stack:
                    square_stack.append(char)
                elif square_stack[-1] == char:
                    square_stack.append(char)
                elif square_stack[-1] != char:
                    square_stack.pop()

            elif char in braces:
                if not braces_stack:
                    braces_stack.append(char)
                elif braces_stack[-1] == char:
                    braces_stack.append(char)
                elif braces_stack[-1] != char:
                    braces_stack.pop()
        if not curly_stack and not square_stack and not braces_stack:
            matched.append("YES")
        else:
            matched.append("NO")
    return matched


values = ['{}[]()', '{[}]}', '{{{([])}}}', '}}}}{{{}}}']
print(braces(values))
