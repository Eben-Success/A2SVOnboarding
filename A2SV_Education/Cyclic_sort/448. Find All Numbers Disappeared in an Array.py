class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            cur = nums[i] - 1

            if nums[i] != nums[cur] and i != cur:
                nums[i], nums[cur] = nums[cur], nums[i]
            else:
                i += 1

        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)

        return res
        
