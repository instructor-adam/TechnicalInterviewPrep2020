from numpy import ndarray, zeros, sum, bool
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        
        """
        Optimization: we only need to store
        the parity of the number, so xor true will
        alternate, starting at zero, as desired.
        """
        arr = zeros((n,m), dtype=bool)
        for c,r in indices:
            arr[:,r]^=True
            arr[c,:]^=True
            
        return int(sum(arr))

