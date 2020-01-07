def reverseOnlyLetters(s):
    position_dict = {}
    arr = []
    stack = []

    for num in range(len(s)):
        if s[num].isalpha():
            arr.append(s[num])
        else:
            position_dict[num] = s[num]

    for num in range(len(s)):
        if num in position_dict.keys():
            stack.append(position_dict[num])
        else:
            stack.append(arr.pop())

    return "".join(stack)