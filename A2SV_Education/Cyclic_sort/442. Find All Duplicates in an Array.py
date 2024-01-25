class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        res = []

        while i < n:
            cur = nums[i] - 1

            if nums[i] != nums[cur] and i != cur:
                nums[i], nums[cur] = nums[cur], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
        
        return res
