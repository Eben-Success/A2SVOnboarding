class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        Time: O(n) | Space: O(1)
        
        1. Use for loop to group the 0s to the left.
        2. Iterate over the array if num is > 0: break.
        3. Set left pointer to i and right pointer to len(nums) -1
        4. Swap if nums[right] is 1
        """
        
        zero_index = 0
        
        for i in range(len(nums)):
            if nums[i] == 0 and zero_index < len(nums):
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
                
        l, r = 0, len(nums) -1
        for i in range(len(nums)):
            if nums[i] > 0:
                l = i
                break
                
        while l < r:
            if nums[r] != 1:
                r -= 1
            else:
                if nums[l] == 1:
                    l += 1
                else:
                    nums[r], nums[l] = nums[l], nums[r]
                    l += 1
                    r -= 1
                    
                
        
                
            
        
        
                
        
