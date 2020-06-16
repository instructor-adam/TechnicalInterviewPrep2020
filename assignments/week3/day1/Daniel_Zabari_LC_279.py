class Solution:
    def numSquares(self, n: int) -> int:
        num_squares = [0]
        for i in range(1, n+1):
            j = 1
            num_squares.append(float("inf"))
            while (j * j) <= i:
                num_squares[i] = min(num_squares[i], num_squares[i-(j*j)]+1)
                if num_squares[i] == 0:
                    break
                j += 1
        return num_squares[n]
