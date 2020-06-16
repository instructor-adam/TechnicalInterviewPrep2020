class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        i = 0
        max_index = 0
        while (i < length) and (i <= max_index):
            potential = nums[i] + i
            if potential > max_index:
                max_index = potential
            if max_index >= (length - 1):
                return True
            i += 1
        return False
