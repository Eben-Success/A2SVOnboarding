class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        [3, 4, 5, 1, 2]
        [5, 1, 2,3 ,4]
        Since the array is rotated, the min will mostly be found at the 
        right.
        1. Check if nums[mid] > nums[right]: move the right pointer.
        2. Else is when nums[mid] <= nums[right]: our min is found
        at the left
        """
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid - 1

            if nums[left] > nums[mid] < nums[right]:
                return nums[mid]

        return nums[left]


        
