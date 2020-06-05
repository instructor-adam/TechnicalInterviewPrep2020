class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = self.binsearch(nums, 0, len(nums), target - .1)
        hi = self.binsearch(nums, 0, len(nums), target + .1)
        if lo >= len(nums):
            return [-1, -1]
        if nums[lo] == target:
            return [lo, hi - 1]
        return [-1, -1]
    def binsearch(self, nums, lo, hi, target):
        mid = (lo + hi) // 2
        if lo >= hi or nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.binsearch(nums, lo, mid, target)
        return self.binsearch(nums, mid+1, hi, target)
