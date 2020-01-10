def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    hash = {}

    for number_index in range(len(nums)):
        if nums[number_index] not in hash:
            hash[nums[number_index]] = [number_index]
        else:
            hash[nums[number_index]].append(number_index)
    for sub_array in hash.values():
        if len(sub_array) < 2:
            continue
        else:
            for index in range(len(sub_array) - 1):
                if abs(sub_array[index] - sub_array[index + 1]) <= k:
                    return True
            return False
