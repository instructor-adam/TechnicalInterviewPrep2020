class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        remove = set()
        returnArray = []

        for i in range(0,len(S)):
            if(S[i] == "("):
                stack.append(i)
            else:
                if(len(stack) == 1):
                    remove.add(stack.pop())
                    remove.add(i)
                else:
                    stack.pop()

        for i in range(0, len(S)):
            if(i not in remove):
                returnArray.append(S[i])

        return("".join(returnArray))

    def findTheDifference(self, s: str, t: str) -> str:
        mySet = {}

        for i in t:
            if i in mySet:
                mySet[i] += 1
            else:
                mySet[i] = 1

        for i in s:
            mySet[i] -= 1

        for i in mySet:
            if(mySet[i] == 1):
                return(i)
