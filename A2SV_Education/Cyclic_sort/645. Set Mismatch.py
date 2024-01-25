class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        while i < n:
            cur = nums[i] - 1

            if nums[i] != nums[cur] and i != cur:
                nums[i], nums[cur] = nums[cur], nums[i]
            else:
                i += 1

        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.extend([nums[i], i + 1])
        return res
        
