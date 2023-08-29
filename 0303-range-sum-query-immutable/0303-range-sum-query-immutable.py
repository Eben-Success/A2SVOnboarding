class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        n = len(self.nums)
        self.prefix = [0] * (n + 1)

        for i in range(1, len(self.prefix)):
            self.prefix[i] = self.prefix[i-1] + self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        
        rangeSum =  self.prefix[right + 1] - self.prefix[left]

        return rangeSum
        
        
        


    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)