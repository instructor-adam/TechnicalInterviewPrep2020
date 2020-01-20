class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = arr[-1]
        for i in reversed(range(0, len(arr))):
            temp = curMax
            if(arr[i] > curMax):
                curMax = arr[i]
            arr[i] = temp
        arr[-1] = -1
        return(arr)

    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        r = ""
        stack = []
        for char in S:
            if(char.isalpha()):
                stack.append(char)
        for i in range(len(S)):
            if(S[i].isalpha()):
                S[i] = stack.pop()
            r+=S[i]
        return(r)
            
