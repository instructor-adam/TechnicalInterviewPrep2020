 # passes 73/75 test cases O(n) time O(1) space 
 def canJump(self, nums):
        moves_left = nums[0]
        for i in range(len(nums)):
            if moves_left == 0:
                moves_left = nums[i]
              
            if nums[i] + i >= len(nums) -1:
                return True
        
            if moves_left == 0 and nums[i] == 0:  
                return False 
        
            moves_left -= 1
            
        return True