class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        pStack = []
        symbol = S[count]
        for symbol in S:
            if symbol == "(":
                S.append(symbol)
            elif pStack == 0 and symbol == ")":
                count+=1
                S.pop()
            elif pStack != 0 and S[count]-1:
                count+=1
            else:
                S.pop()
                #parenthesis are balanced
        count += 1
//These are the notes I wrote down while problem-solving:
        //Stack and a counter
//After each push, check if they're balanced
//Push open parentehsis onto the stack
//Pop the stack when a closed parenthesis is found
//if stack is empty and S[i] is closed parenthesiis:
//increment count
//if at end of string and the stack is not empty,
//increment count