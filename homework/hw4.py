class Solution:
    def reduceEmail(self, email: str) -> str:
        rString = ""
        t = -1
        passedPlus = False

        for i in range(len(email)):
            if(email[i] == "@"):
                t = i
                break
            elif(email[i] == "+"):
                passedPlus = True
            elif((email[i] != ".") and (passedPlus == False)):
                rString+=(email[i])

        for i in range(t, len(email)):
            rString+=email[i]
        return(rString)


    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            temp = self.reduceEmail(email)
            seen.add(temp)
        return(len(seen))
