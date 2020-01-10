def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hash_set = set()
    
    for num in nums1:
        if num in nums2:
            hash_set.add(num)
    return hash_set