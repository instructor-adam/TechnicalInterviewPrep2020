class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        max_row = len(matrix)
        if max_row == 0:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while (row < max_row) and (col >= 0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
        return False
