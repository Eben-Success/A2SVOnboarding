class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixes = None # list[int] 
        self.compute_prefixes()
    
    def compute_prefixes(self):
        self.prefixes = [0] * len(self.nums)
        self.prefixes[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.prefixes[i] = self.prefixes[i - 1] + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right] - self.prefixes[left] + self.nums[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
