def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    hash = {}

    for num in nums:
        if num not in hash:
            hash[num] = 1
        else:
            hash[num] += 1

    min_index = min(hash.keys())

    for index in range(len(nums)):
        nums[index] = min_index
        hash[min_index] -= 1

        if hash[min_index] == 0 and min_index + 1 not in hash:
            min_index += 2

        elif hash[min_index] == 0:
            min_index += 1