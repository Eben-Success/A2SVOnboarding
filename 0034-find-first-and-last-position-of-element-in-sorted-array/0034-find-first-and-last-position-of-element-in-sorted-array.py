class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.bisect_left(nums, target)
        last = self.bisect_right(nums, target)
        
        return [first, last]
    
    def bisect_left(self, nums: List[int], target: int) -> int:
        # minimization: high
        n = len(nums) 
        low, high = -1, n
        
        while (low + 1) < high:
            mid = ((high - low)//2) + low
            
            if nums[mid] >= target:
                high = mid
            else:
                low = mid
        if high == n or nums[high] != target:
            return -1
        
        return high
    
    
    def bisect_right(self, nums: List[int], target: int) -> int:
        # maximization: low
        n = len(nums)
        low, high = -1, n
        
        while (low + 1) < high:
            mid = ((high - low) // 2) + low
            
            if nums[mid] <= target:
                low = mid
            else:
                high = mid 
                
        if low == -1 or nums[low] != target:
            return -1
        return low
        