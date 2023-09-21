class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # minimization problem: high
        
        n = len(nums)
        low, high = -1, n 
        
        while low + 1 < high:
            mid = ((high - low)//2) + low
            
            if self.isGreaterOrEqual(nums[mid], target):
                high = mid
            else:
                low = mid
                
        return high
    
    
    def isGreaterOrEqual(self, num: int, target: int) -> bool:
        return num >= target
        