class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [0, 1, 0, 3, 12]
        
        read, write = 0, 0
        
        while read < len(nums):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1
                
