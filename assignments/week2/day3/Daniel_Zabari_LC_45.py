class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        prev_max_index = 0
        current_max_index = 0
        jumps = 0
        for i, num in enumerate(nums[:-1]):
            current_max_index = max(current_max_index, i+num)
            if prev_max_index == i:
                prev_max_index = current_max_index
                jumps += 1
        return jumps
