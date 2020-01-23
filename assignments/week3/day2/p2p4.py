class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myMax = '-inf'
        mySet = set()
        for num in nums:
            mySet.add(num)
            if num > myMax:
                myMax=num
    for i in range()
#         #sort the array in place
#         nums = sorted(nums)
#         print(nums)
#         #if 
# #         index = 0
# #         end = len(nums)
# #         for num in nums: 
# #             if nums[end - 1] == end - 1:
# #                 return num
# #             while end - index > 1:
# #                 middle = (index+end)/2
# I think my approach was to sort the array 
# add them to a set and return the number not in the set
# or return the index
# because if the list is sorted, 
# the number would equal the index.
# if it doesn't, I could return the index