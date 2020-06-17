class Solution:
    stone_memo = {}
    def canCross(self, stones: List[int]) -> bool:
        self.stone_memo = {}
        if len(stones) <= 1:
            return True
        if stones[1] != 1:
            return False
        return self.cross_helper(stones, 1, 0, 1)

    def cross_helper(self, stones: List[int], index: int, position: int, jump: int) -> bool:
        print(index, position, jump)
        if index == len(stones):
            return position == stones[-1]
        stone = stones[index] 
        if (position + jump + 1) < stone: 
            return False
        if (position, stone, jump) in self.stone_memo:
            return self.stone_memo[(position, stone, jump)]
        skip = self.cross_helper(stones, index+1, position, jump)
        if skip is True:
            self.stone_memo[stone] = True
            return True
        ans = False
        if stone == (position + jump):
            ans = self.cross_helper(stones, index+1, stone, jump)
        elif stone == (position + jump + 1):
            ans = self.cross_helper(stones, index+1, stone, jump+1)
            jump = jump + 1
        elif stone == (position + jump - 1):
            ans = self.cross_helper(stones, index+1, stone, jump-1)
            jump = jump - 1
        self.stone_memo[(position, stone, jump)] = ans
        return ans
