class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seenFixedLength = {}
        repeated = []

        for i in range(len(s)):
            j = i + 1
            for j in range(len(s)+1):
                ss = s[i:j]
                if len(ss) is 10:
                    if ss in seenFixedLength.keys():
                        #count number of times substring has been seen 
                        seenFixedLength[ss] = seenFixedLength[ss] + 1
                    else:
                        #observe substring for first time 
                        seenFixedLength[ss] = 1
          
        for key in seenFixedLength:
            if seenFixedLength[key] > 1:
                repeated.append(key)
         
        return repeated
# soltuion runs in O(N^2) time. passes 31 of 32 
# test cases where the last test case exceeds time limit
# solution is correct but not very efficient 