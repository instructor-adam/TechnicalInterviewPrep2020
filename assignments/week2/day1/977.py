from bisect import bisect_left
from collections import deque
class Solution1(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A = deque([a**2 for a in A])
        pos = A
        neg = deque()
        while pos[0] < 0:
            neg.append(pos[0])
            pos.popleft()
            
        ret = []
        # merge
        while (pos or neg):
            if not neg:
                ret.extend(pos)
                return ret
            if not pos:
                ret.extend(neg)
                return ret
            p = pos.popleft()
            n = neg.popleft()
            print(p,n)
            if p < n:
               neg.appendleft(n)
               ret.append(p)
            else:
               pos.appendleft(p)
               ret.append(n)
           
        return ret
        
class Solution2(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        ret = sorted([a**2 for a in A])
        
           
        return ret
        

# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-using-deque-beats-100
# linear time, linear space 
def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)
