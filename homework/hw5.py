class Solution:
    # Part 1
    def decodeString(self, s: str) -> str:
        stack = []
        pushing = False
        match = 0
        rString = ""
        num = ""

        if '[' not in s:
            return s

        for char in s:
            if(pushing):
                if(char == ']'):
                    match -= 1
                    if(match == 0):
                        rString += int(num)*self.decodeString("".join(stack))
                        pushing = False
                        num = ""
                        stack = []
                        continue
                elif(char == '['):
                    match += 1
                stack.append(char)
            else:
                if(char == '['):
                    match += 1
                    pushing = True
                elif(char in '0123456789'):
                    num+=char
                else:
                    rString+=char
            print(num, char, pushing, match, stack)
        return rString

# Part 2
class NestedIterator:
    allItems = []
    current = 0

    def expand(self, nestedList):
        t = []
        for i in nestedList:
            if(i.isInteger()):
                t.append(i.getInteger())
            else:
                c = self.expand(i.getList())
                for i in c:
                    t.append(i)
        return t

    def __init__(self, nestedList: [NestedInteger]):
        self.allItems = self.expand(nestedList)
        self.current = 0

    def next(self) -> int:
        t = self.allItems[self.current]
        self.current += 1
        return t

    def hasNext(self) -> bool:
        return self.current < len(self.allItems)    
