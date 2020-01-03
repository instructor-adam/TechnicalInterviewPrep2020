#!/usr/bin/env python3


def balancedStringSplit(s: str) -> int:
    stack = []
    count = 0

    for char in s:
        if len(stack) == 0:
            stack.append(char)

        elif stack[len(stack) - 1] != char:
            stack.pop()
            if len(stack) == 0:
                count += 1

        elif stack[len(stack) - 1] == char:
            stack.append(char)

    return count