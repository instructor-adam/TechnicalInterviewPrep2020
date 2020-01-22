class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return n
        i = 1
        fI = 1
        fP = 1
        while i < n:
            nF = fI + fP
            fP = fI
            fI = nF
            i+=1

        return fI

#     cached_results = {}
#     def climbStairs(self, n: int) -> int:
#         if(n == 1 or n == 2):
#             return n;
#         elif(n in self.cached_results):
#             return self.cached_results[n]
#         result = self.climbStairs(n-1) + self.climbStairs(n-2)
#         self.cached_results[n] = result
#         return result

        
