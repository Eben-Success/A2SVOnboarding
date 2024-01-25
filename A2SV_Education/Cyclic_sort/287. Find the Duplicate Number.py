class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            cur = nums[i] - 1

            if nums[i] != nums[cur] and i != cur:
                nums[i], nums[cur] = nums[cur], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                return nums[i]
                

        
