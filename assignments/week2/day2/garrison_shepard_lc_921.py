def minAddToMakeValid(self, S):  
    if len(S) == 0:
        return 0
    
    stack = [] 
    stack.append(S[0])
    for i in range(1, len(S)):
        if len(stack) > 0:
            if (stack[-1] + S[i]) == '()':
                stack.pop()
            else:
                stack.append(S[i])
        else:
            stack.append(S[i])
    return len(stack)